from random import randint

# Алгоритм сложностью O(log n^2)

N = 10
def choose_sort(row):
    n = len(row)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if row[j] < row[m]:
                m = j
        row[i], row[m] = row[m], row[i]


arr = [randint(1, 99) for i in range(N)]

choose_sort(arr)
print(arr)


# Алгоритм сложностью O(log n)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print(gcd(6, 18))
