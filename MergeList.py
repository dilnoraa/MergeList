
# merging 2 lists without using extend method
# O(len(A)+len(B))

def merge(list_A, list_B):
    i = 0
    j = 0
    list_C = []
    while i < len(list_A) and j < len(list_B):
        if list_A[i] < list_B[j]:
            list_C.append(list_A[i])
            i += 1
        else:
            list_C.append(list_B[j])
            j += 1
    if i < len(list_A):
        list_C += list_A[i:]
    if j < len(list_B):
        list_C += list_B[j:]
    return list_C


A = [1, 13, 25, 70, 96]
B = [2, 4, 6, 8, 15]
C = merge(A, B)
print(C)
