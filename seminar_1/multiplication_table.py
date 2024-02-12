"""Multiplication table."""

for i in range(2, 10):
    for j in range(2, 11):
        print(f'{i} x {j} = {i*j}', sep='')
    print()
