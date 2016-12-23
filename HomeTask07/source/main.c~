#include "threadpool.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int rec_max;

int funccmp(const void* val1, const void* val2) {
  return *(int*)val1 - *(int*)val2;
}

void swap(int* a, int *b) {
  int t = *a;
  *a = *b;
  *b = t;
}

cur_data_* init_cur_data(int* data, int len, int rec, threadpool_* pool) {
  cur_data_* task = malloc(sizeof(cur_data_*));
  
  task->pool = pool;
  task->len = len;
  task->rec = rec;
  task->data = data;
  task->left = task->right = NULL;
  
  return task;
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

  while (l >= r) {
    while (cur_data->data[l] < part) l++;
    while (cur_data->data[l] > part) r--;
    if (l <= r)
      swap(cur_data->data[l++], cur_data->data[r--]);
  }

  cur_data_* left = init_cur_data(cur_data->data, l, cur_data->rec + 1, data->pool);
  cur_data_* right = init_cur_data(cur_data->data + l, cur_data->len - l, sort_task->rec + 1, data->pool);

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
  free(task->args);
  free(task);
}


bool check(int* data, int size) {    
  for (i = 0; i < n - 1; i++) 
    if (data[i] > data[i + 1]) 
      return false;
  return true;
}

int main (int argc, char** argv) {
  int thr_num = atoi(argv[1]);
  size_t size = atoi(argv[2]);
  rec_max = atoi(argv[3]);

  srand(42);

  int* data = malloc(size * sizeof(int));

  for (int i = 0; i < size; i++)
    data[i] = rand();

  threadpool_ pool;        
  thpool_init(&pool, size);

  task_* main_task = task_new(&pool, sort, init_cur_data(void*)((mas, n, 0, &pool)));
  thpool_submit(&pool, task);
  
  dfs(task);
    
  if (!check(data, size))
    exit(1); 
  
  thpool_finit(&pool);

  free(data);
  pthread_exit(NULL);  

  return 0;
}

