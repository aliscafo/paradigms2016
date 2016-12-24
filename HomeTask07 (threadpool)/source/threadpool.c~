#include "threadpool.h"

static volatile bool cont = true;

void* taskfunc (void* data) {
  wsqueue_* queue = data;

  while (cont || queue_size(&queue->squeue.queue)) {
    struct list_node* node;
    pthread_mutex_lock(&queue->squeue.mutex);
    
    while (cont && !queue_size(&queue->squeue.queue))
      pthread_cond_wait(&queue->cond, &queue->squeue.mutex);  
    
    node = queue_pop(&queue->squeue.queue);
    pthread_mutex_unlock(&queue->squeue.mutex);

    if (node) {
      task_ *task = (task_ *)node;
      pthread_mutex_lock(&task->mutex);
      task->f((void*)(task->arg));
      task->completed = true;
      pthread_cond_signal(&task->cond);
      pthread_mutex_unlock(&task->mutex);
    } 
  }

  return NULL;
}

task_* task_new(threadpool_* pool, void (*func)(void*), void* args) {
    task_* t = malloc(sizeof(task_));
    t->pool = pool;
    t->f = func;
    t->arg = args;
    t->completed = false;
    t->left = t->right = NULL;
    pthread_mutex_init(&t->mutex, NULL);
    pthread_cond_init(&t->cond, NULL);
    return t;
}


void thpool_init(threadpool_ *pool, size_t threads_nm) {
  int i; 
  pool->num = threads_nm;
  /*pool->queue = malloc(sizeof(wsqueue_));*/
  pool->threads = (pthread_t*)malloc(sizeof(pthread_t) * threads_nm);
  wsqueue_init(&pool->queue);
  for (i = 0; i < threads_nm; i++)
    pthread_create(&pool->threads[i], NULL, taskfunc, &pool->queue);
}


void thpool_submit(struct ThreadPool *pool, struct Task *task) {
  wsqueue_push(&pool->queue, (struct list_node*)task);
}


void thpool_wait(struct Task *task) {
  if (!task) 
    return;
  pthread_mutex_lock(&task->mutex);
  while(!task->completed)
    pthread_cond_wait(&task->cond, &task->mutex); 
  pthread_mutex_unlock(&task->mutex);
}


void thpool_finit(struct ThreadPool *pool) {
  int i;
  pthread_mutex_lock(&pool->queue.squeue.mutex);
  cont = false;    
  /*pthread_cond_broadcast(&(pool->queue->cond));*/
  pthread_mutex_unlock(&pool->queue.squeue.mutex);

  wsqueue_notify_all(&pool->queue);

  for (i = 0; i < pool->num; i++) 
    pthread_join(pool->threads[i], NULL);

  free(pool->threads);
  wsqueue_finit(&pool->queue);
}
                            
