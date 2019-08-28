PROGS:=$(filter-out *.%,$(shell cat .gitignore)) $(wildcard *.py)
PIDS=$(wildcard *.pid)
CFLAGS=-Wall

all: $(PROGS)

%.pid: %
	./$< > $*.out & \
		echo $$! > $@

%.kill:
	-kill `< $*.pid`
	rm $*.pid

run: $(PROGS:=.pid)
kill: $(PIDS:.pid=.kill)
