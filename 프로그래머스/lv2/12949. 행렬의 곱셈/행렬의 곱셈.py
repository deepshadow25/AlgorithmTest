def solution(arr1, arr2):
    r = len(arr1)
    c = len(arr2[0])
    result = [[0 for col in range(c)] for row in range(r)]
    
    for i, x in enumerate(arr1):
        for k, y in enumerate(x):
            for j in range(c):
                result[i][j] += arr1[i][k] * arr2[k][j]
    
    return result        