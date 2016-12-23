CC      ?= gcc
CFLAGS  ?= -Wall -Wextra -Werror -ansi -pedantic
LDFLAGS ?= -lpthread

all: pqsort bin

bin:
	mkdir -p bin

pqsort: bin/main.o bin/linkedlist.o bin/queue.o bin/squeue.o bin/wsqueue.o bin/threadpool.o
	$(CC) bin/main.o bin/linkedlist.o bin/queue.o bin/squeue.o \
		  bin/threadpool.o bin/wsqueue.o $(LDFLAGS) -o pqsort 

bin/main.o: source/main.c
	$(CC) -c source/main.c $(CFLAGS) -o bin/main.o

bin/threadpool.o: source/threadpool.c
	$(CC) -c source/threadpool.c $(CFLAGS) -o bin/threadpool.o

bin/linkedlist.o: source/linkedlist.c
	$(CC) -c source/linkedlist.c $(CFLAGS) -o bin/linkedlist.o

bin/queue.o: source/queue.c
	$(CC) -c source/queue.c $(CFLAGS) -o bin/queue.o

bin/squeue.o: source/squeue.c
	$(CC) -c source/squeue.c $(CFLAGS) -o bin/squeue.o

bin/wsqueue.o: source/wsqueue.c
	$(CC) -c source/wsqueue.c $(CFLAGS) -o bin/wsqueue.o

clean:
	rm bin pqsort

.PHONY: clean