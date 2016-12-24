#ifndef __THREADPOOL_H__
#define __THREADPOOL_H__

#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "wsqueue.h"

typedef struct ThreadPool {
  pthread_t* threads;
  wsqueue_ queue;
  size_t num;
} threadpool_ ;

typedef struct Task {
  void (*f)(void *); 
  void* arg; 
  
  struct Task* left;
  struct Task* right;

  threadpool_* pool;
  bool completed;
  pthread_cond_t cond;
  pthread_mutex_t mutex;
} task_ ;

typedef struct cur_data {
    int* data;
    int rec, len;
    threadpool_* pool;
    task_* left, right;
} cur_data_;
 
task_* task_new(threadpool_* pool, void (*func)(void*), void* args);

void thpool_init(struct ThreadPool *pool, unsigned threads_nm);
void thpool_submit(struct ThreadPool *pool, struct Task *task);
void thpool_wait(struct Task *task);
void thpool_finit(struct ThreadPool *pool);

#endif /*__THREADPOOL_H__*/
