# Bubble Sort
# For the function: First agument is the list, Second argument is either 'ascending' or 'descending' (depending on how you wish to sort the list)

def bubble_sort(li, method):
    length = len(li)
    end = False

    while end == False:
        count = 0
        for i in range(length-1):
            num_now = li[i]
            num_next = li[i+1]

            cond_1 = False
            cond_2 = False
            
            if method == 'ascending':
                if num_now > num_next:
                    li[i] = num_next
                    li[i+1] = num_now
                    cond_1 = True
            elif method == 'descending':
                if num_now < num_next:
                    li[i] = num_next
                    li[i+1] = num_now
                    cond_2 = True

            if cond_1 == False and cond_2 == False:
                count += 1
                
        if count == length-1:
            end = True

    return li

# Example
print(bubble_sort([5, 3, 8, 6, 7, 2], 'descending'))
