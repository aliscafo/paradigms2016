#ifndef __THREADPOOL_H__
#define __THREADPOOL_H__

#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include "wsqueue.h"

typedef struct ThreadPool {
  void* threads;
  wsqueue_ t_queue;
  size_t num;
} threadpool_ ;

typedef struct Task {
  void (*f)(void *); 
  void* arg; 
  
  struct task* left, right;

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
 
void thpool_init(struct ThreadPool *pool, unsigned threads_nm);
void thpool_submit(struct ThreadPool *pool, struct Task *task);
void thpool_wait(struct Task *task);
void thpool_finit(struct ThreadPool *pool);

#endif /*__THREADPOOL_H__*/