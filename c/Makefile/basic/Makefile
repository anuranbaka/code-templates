# Taken from http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/ , which appears to be public domain. Modified to add a bin dir and src dir

IDIR = include
ODIR = obj
LDIR = lib
BDIR = bin
SDIR = src

CC=gcc
CFLAGS=-I$(IDIR)

_DEPS = hellomake.h
DEPS = $(patsubst %,$(IDIR)/%,$(_DEPS))

_OBJ = hellomake.o hellofunc.o 
OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))



$(ODIR)/%.o: $(SDIR)%.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

$(BDIR)/program: $(OBJ)
	gcc -o $@ $^ $(CFLAGS)

.PHONY: clean

clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~ $(BDIR)/* 
