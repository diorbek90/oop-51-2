lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def binary_search(lst, target):
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == target:
            return mid

        elif lst[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


print(binary_search(lst, 9))


# O(n)
def find_element(lst, target):
    for i in lst:
        if i == target:
            return True

    return False


lst3 = [9, 2, 5, 1, 5, 2, 8, 7, 45]

print(lst3.sort())


# O(n**2) Квадратичное время

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):

            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


bubble_sort(lst=lst3)
print(lst3)
