def print_items(a,b):
    for i in range(a):
        print(i)

    for j in range(b):          # o(2n)-->o(n)  2 is constant is drop
        print(j)

print_items(1, 10)
