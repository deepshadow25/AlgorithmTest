def solution(arr):
    stack = [-1]
    for i in range(len(arr)):
        if stack[-1] != arr[i]:
            stack.append(arr[i])
    stack.pop(0)
    return stack