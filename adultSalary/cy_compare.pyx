# cy_compare.pyx
def cy_duplicate_count(list1, list2):
    cdef int i, j, cnt = 0
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                cnt += 1
                break
    return cnt

