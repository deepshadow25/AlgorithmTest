mod = 1000000007

def dot_product(arr1, arr2):
    l = len(arr1)
    new_arr = [[0] * l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            for k in range(l):
                new_arr[i][j] += arr1[i][k] * arr2[k][j]
            new_arr[i][j] %= mod
    return new_arr

def matrix_product(arr, L):
    l = len(arr)
    result = [0] * l
    for i in range(l):
        for j in range(l):
            result[i] += arr[i][j] * L[-j-1]
            result[i] %= mod
    return result

def solution(n):
    S = [1, 3, 10, 23, 62, 170]
    if n < 7:
        return S[n-1]
    
    arr = [[1, 2, 6, 1, 0, -1]]
    for i in range(5):
        L = [0] * 6
        L[i] = 1
        arr.append(L)
        
    mtx = [row[:] for row in arr]
    r_matrix = [[0] * 6 for _ in range(6)]
    for i in range(6):
        r_matrix[i][i] = 1
        
    count = n - 3
    while count > 0:
        if count % 2:
            r_matrix = dot_product(r_matrix, mtx)
        mtx = dot_product(mtx, mtx)
        count //= 2
    return matrix_product(r_matrix, S)[3]
