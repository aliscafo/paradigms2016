#include "linkedlist.h"

void list_insert(struct list_node *node, struct list_node *new)
{
	new->prev = node;
	new->next = node->next;
	node->next->prev = new;
	node->next = new;
}

void list_remove(struct list_node *node)
{
	node->prev->next = node->next;
	node->next->prev = node->prev;
}