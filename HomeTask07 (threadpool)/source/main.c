#include "threadpool.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int rec_max;

int funccmp(const void* val1, const void* val2) {
  return *(int*)val1 - *(int*)val2;
}

void swap(int* a, int* b) {
  int t = *a;
  *a = *b;
  *b = t;
}

cur_data_* init_cur_data(int* data, int len, int rec, threadpool_* pool) {
  cur_data_* tsk = malloc(sizeof(cur_data_));
  
  tsk->pool = pool;
  tsk->len = len;
  tsk->rec = rec;
  tsk->data = data;
  
  return tsk;
}

void sort(void* data) {
  task_* task = (task_*)(data);
  cur_data_* cur_data = (cur_data_*)(task->arg);
  
  if (cur_data->rec == rec_max) {
    qsort(cur_data->data, cur_data->len, sizeof(int), funccmp);
    return;
  }

  if (cur_data->len < 2) return;

  int part = cur_data->data[cur_data->len >> 1];

  int l = 0, r = cur_data->len - 1;

  while (l <= r) {
    while (cur_data->data[l] < part) l++;
    while (cur_data->data[r] > part) r--;
    if (l <= r)
      swap(&(cur_data->data[l++]), &(cur_data->data[r--]));
  }

  cur_data_* left = init_cur_data(cur_data->data, l, cur_data->rec + 1, cur_data->pool);
  cur_data_* right = init_cur_data(cur_data->data + l, cur_data->len - l, cur_data->rec + 1, cur_data->pool);

  task_* t_left = task_new(task->pool, sort, (void*)(left));
  task_* t_right = task_new(task->pool, sort, (void*)(right));
  
  task->left = t_left;
  task->right = t_right;

  thpool_submit(task->pool, t_left);
  thpool_submit(task->pool, t_right);
}


void dfs(task_* task) {
  if (!task) return;

  thpool_wait(task);
  
  dfs(task->left);
  dfs(task->right);
  free(task->arg);
  free(task);
}


bool check(int* data, int size) {    
  int i;
  for (i = 0; i < size - 1; i++) {
    if (data[i] > data[i + 1]) 
      return false;
    /*if (i < 5) printf("%i\n", data[i]);*/
  }

  return true;
}

int main (int argc, char** argv) {
  int thr_num = atoi(argv[1]);
  size_t size = atoi(argv[2]);
  rec_max = atoi(argv[3]);
  int i = 0;
  
  srand(42);

  int* data = malloc(size * sizeof(int));

  for (i = 0; i < size; i++)
    data[i] = rand();

  threadpool_ pool;        
  thpool_init(&pool, thr_num);

  task_* main_task = task_new(&pool, sort, (void*)(init_cur_data(data, size, 0, &pool)));

  thpool_submit(&pool, main_task);
 
  dfs(main_task);

  if (!check(data, size)) {
    free(data);
    exit(1); 
  }
  
  thpool_finit(&pool);

  free(data);
  
  pthread_exit(NULL);  
  return 0;
}

