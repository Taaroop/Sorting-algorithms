def linear_sort(li):
    length = len(li)
    li_sorted = []
    for i in range(length):
        x_min = li[0]
        for j in li:
            if j < x_min:
                x_min = j
        li_sorted.append(x_min)
        li.remove(x_min)
    return li_sorted

# Test run
li = [99, 78, 34, 100, 0, 2, 222, 90, 65]
print(linear_sort(li))
