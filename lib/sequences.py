#!/usr/bin/env python3

# With range:

def print_fibonacci(length):
    pass
    fibonacci_sequence = []
    if length > 0:
        fibonacci_sequence.append(0)
        if length > 1:
            fibonacci_sequence.append(1)
            if length > 2:
                for i in range(2, length):
                    fibonacci_sequence.append(
                        fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])

    print(fibonacci_sequence)

# Without range:

# def print_fibonacci(length):
#     fibonacci_sequence = []
#     if length > 0:
#         fibonacci_sequence.append(0)
#         if length > 1:
#             fibonacci_sequence.append(1)
#             if length > 2:
#                 i = 2
#                 while i < length:
#                     fibonacci_sequence.append(
#                         fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
#                     i += 1

#     print(fibonacci_sequence)