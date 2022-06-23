#!/usr/bin/env python

def print_fibonacci(length):

    fibonacci_sequence = list()
    if length >= 1:
        fibonacci_sequence.append(0)

        if length >= 2:
            fibonacci_sequence.append(1)

            if length >= 3:

                for n in range(2, length):
                    fibonacci_sequence.append(
                        fibonacci_sequence[n-1] + fibonacci_sequence[n -2]
                    )

    for n in fibonacci_sequence:
        print(n)
