all: example.so

CFLAGS += -fPIC -g -Wall -O3

example.so: example.o
	$(CC) $(CFLAGS) $(CPPFLAGS) $(LDFLAGS) -shared -o $@ $^

clean:
	${RM} example.so example.o

.PHONY: clean
