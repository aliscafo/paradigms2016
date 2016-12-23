#include "threadpool.h"

static volatile bool cont = true;

void* taskfunc (void* data) {
  wsqueue_ *queue = data;

  while (cont || queue_size(&queue->squeue.queue)) {
    struct list_node* node;
    pthread_mutex_lock(&queue->mutex);
    
    while (cont && !queue_size(&queue->squeue.queue))
      pthread_cond_wait(&queue->cond, &queue->squeue.mutex);  
    
    node = queue_pop(&queue->squeue.queue);
    pthread_mutex_unlock(&queue->mutex);

    if (node) {
      task_ *task = (task_ *)node;
      pthread_mutex_lock(&task->mutex);
      task->completed = true;
      pthread_cond_signal(&task->cond);
      pthread_mutex_unlock(&task->mutex);
    } 
  }

  return NULL;
}

task_* task_new(threadpool_* pool, void (*func)(void*), void* args) {
    task_* t = malloc(sizeof(task_));
    //task->pool = pool;
    task->f = func;
    task->arg = args;
    task->completed = false;
    task->left = task->right = NULL;
    pthread_mutex_init(&task->mutex, NULL);
    pthread_cond_init(&task->cond, NULL);
    return task;
}


void thpool_init(struct ThreadPool *pool, size_t threads_nm) {
  pool->num = threads_nm;
  pool->threads = (pthread_t*)malloc(sizeof(pthread_t) * threads_nm);
  wsqueue_init(&pool->queue);
  for (int i = 0; i < threads_nm; i++)
    pthread_create(&pool->threads[i], NULL, taskfunc, pool);
}


void thpool_submit(struct ThreadPool *pool, struct Task *task) {
  wsqueue_push(&pool->queue, (struct list_node*)task);
}


void thpool_wait(struct Task *task) {
  pthread_mutex_lock(&task->mutex);
  while(!task->completed)
    pthread_cond_wait(&task->cond, &task->mutex); 
  pthread_mutex_unlock(&task->mutex);

}


void thpool_finit(struct ThreadPool *pool) {
  pthread_mutex_lock(&pool->queue->squeue.mutex);
  cont = false;    
  pthread_mutex_unlock(&pool->queue->squeue.mutex);

  for (int i = 0; i < pool->num; i++) 
    pthread_join(pool->threads[i], NULL);

  wsqueue_finit(&pool->queue);
  free(pool->threads);
}
                            
