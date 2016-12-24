CC      ?= gcc
CFLAGS  ?= -ansi 
LDFLAGS ?= -lpthread

all: bin pqsort

bin:
	mkdir -p bin

pqsort: bin/main.o bin/linkedlist.o bin/queue.o bin/squeue.o bin/wsqueue.o bin/threadpool.o
	$(CC) bin/main.o bin/linkedlist.o bin/queue.o bin/squeue.o \
		bin/threadpool.o bin/wsqueue.o $(LDFLAGS) -o pqsort 

bin/main.o: source/main.c
	$(CC) -c -I include source/main.c $(CFLAGS) -o bin/main.o

bin/threadpool.o: source/threadpool.c
	$(CC) -c -I include source/threadpool.c $(CFLAGS) -o bin/threadpool.o

bin/linkedlist.o: source/linkedlist.c
	$(CC) -c -I include source/linkedlist.c $(CFLAGS) -o bin/linkedlist.o

bin/queue.o: source/queue.c
	$(CC) -c -I include source/queue.c $(CFLAGS) -o bin/queue.o

bin/squeue.o: source/squeue.c
	$(CC) -c -I include source/squeue.c $(CFLAGS) -o bin/squeue.o

bin/wsqueue.o: source/wsqueue.c
	$(CC) -c -I include source/wsqueue.c $(CFLAGS) -o bin/wsqueue.o

clean:
	rm -rf bin pqsort

.PHONY: clean
