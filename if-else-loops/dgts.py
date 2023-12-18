#!/usr/bin/env python3
for tens_digit in range(10):
    for ones_digit in range(tens_digit +1, 10):
        print(f"{tens_digit}{ones_digit:01d}", end="," if (tens_digit, ones_digit) != (8,9) else "\n")

