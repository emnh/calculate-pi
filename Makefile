CC = gcc
CFLAGS = -Wall -Wextra -pedantic -std=c11
LIBS = -lmpfr -lgmp

TARGET = calc_pi_arb

all: $(TARGET)

$(TARGET): calc_pi_arb.c
	$(CC) $(CFLAGS) -o $(TARGET) calc_pi_arb.c $(LIBS)

clean:
	rm -f $(TARGET)
