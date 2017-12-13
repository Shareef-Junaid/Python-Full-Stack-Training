def arr_slice(x, y, a):
    i = x
    a_slice = []
    while i <= y:
        a_slice.append(a[i])
        i = i + 1

    return a_slice


arr_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

s = arr_slice(0, 3, arr_a)
print(s)