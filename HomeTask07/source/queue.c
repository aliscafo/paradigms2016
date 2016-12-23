#include <string.h>
#include "queue.h"

void queue_init(struct queue *queue)
{
	queue->head.prev = &queue->head;
	queue->head.next = &queue->head;
	queue->size = 0;
}

unsigned long queue_size(struct queue *queue)
{
	return queue->size;
}

void queue_push(struct queue *queue, struct list_node *node)
{
	list_insert(&queue->head, node);
	queue->size += 1;
}

struct list_node *queue_pop(struct queue *queue)
{
	struct list_node *node = queue->head.prev;

	if (!queue_size(queue))
		return NULL;
	list_remove(node);
	queue->size -= 1;
	return node;
}