#include "wsqueue.h"

void wsqueue_init(struct wsqueue *queue)
{
	squeue_init(&queue->squeue);
	pthread_cond_init(&queue->cond, NULL);
}

void wsqueue_finit(struct wsqueue *queue)
{
	pthread_cond_destroy(&queue->cond);
	squeue_finit(&queue->squeue);
}

void wsqueue_push(struct wsqueue *queue, struct list_node *node)
{
	pthread_mutex_lock(&queue->squeue.mutex);
	queue_push(&queue->squeue.queue, node);
	pthread_cond_signal(&queue->cond);
	pthread_mutex_unlock(&queue->squeue.mutex);
}

struct list_node* wsqueue_pop(struct wsqueue *queue)
{
	return squeue_pop(&queue->squeue);
}

int wsqueue_wait(struct wsqueue *queue)
{
	int rc = 0;

	pthread_mutex_lock(&queue->squeue.mutex);
	while (!queue_size(&queue->squeue.queue))
		pthread_cond_wait(&queue->cond, &queue->squeue.mutex);
	rc = queue_size(&queue->squeue.queue) != 0;
	pthread_mutex_unlock(&queue->squeue.mutex);
	return rc;
}

void wsqueue_notify(struct wsqueue *queue)
{
	pthread_mutex_lock(&queue->squeue.mutex);
	pthread_cond_signal(&queue->cond);
	pthread_mutex_unlock(&queue->squeue.mutex);
}

void wsqueue_notify_all(struct wsqueue *queue)
{
	pthread_mutex_lock(&queue->squeue.mutex);
	pthread_cond_broadcast(&queue->cond);
	pthread_mutex_unlock(&queue->squeue.mutex);
}
