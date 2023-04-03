def solution(array, n):
    array = sorted(array)
    abs_arr = [abs(n-array[i]) for i in range(len(array))]
    for j in range(len(abs_arr)):
        if abs_arr[j]==min(abs_arr):
            return array[j]
    