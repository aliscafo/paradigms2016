#ifndef __QUEUE_H__
#define __QUEUE_H__

#include "linkedlist.h"

struct queue {
	struct list_node head;
	unsigned long size;
};

void queue_init(struct queue *queue);
unsigned long queue_size(struct queue *queue);
void queue_push(struct queue *queue, struct list_node *node);
struct list_node *queue_pop(struct queue *queue);

#endif /*__QUEUE_H__*/