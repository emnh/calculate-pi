CC = gcc
CFLAGS = -Wall -Wextra -pedantic -std=c11
LIBS = -lmpfr -lgmp -lm

TARGET = calc_pi_arb

all: $(TARGET) gmp-chudnovsky

gmp-chudnovsky: gmp-chudnovsky.c
	$(CC) $(CFLAGS) -o $@ $< $(LIBS)

$(TARGET): calc_pi_arb.c
	$(CC) $(CFLAGS) -o $(TARGET) calc_pi_arb.c $(LIBS)

clean:
	rm -f $(TARGET)
