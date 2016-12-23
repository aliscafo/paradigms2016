#include "squeue.h"

void squeue_init(struct squeue *squeue)
{
	queue_init(&squeue->queue);
	pthread_mutex_init(&squeue->mutex, NULL);
}

void squeue_finit(struct squeue *squeue)
{
	pthread_mutex_destroy(&squeue->mutex);
}

void squeue_push(struct squeue *squeue, struct list_node *node)
{
	pthread_mutex_lock(&squeue->mutex);
	queue_push(&squeue->queue, node);
	pthread_mutex_unlock(&squeue->mutex);
}

struct list_node *squeue_pop(struct squeue *squeue)
{
	struct list_node *node;

	pthread_mutex_lock(&squeue->mutex);
	node = queue_pop(&squeue->queue);
	pthread_mutex_unlock(&squeue->mutex);
	return node;
}