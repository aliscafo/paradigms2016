#ifndef __LINKED_LIST_H__
#define __LINKED_LIST_H__

struct list_node {
	struct list_node *next;
	struct list_node *prev;
};

void list_insert(struct list_node *node, struct list_node *new_node);
void list_remove(struct list_node *node);

#endif /*__LINKED_LIST_H__*/