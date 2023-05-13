student = [i for i in range(1, 31)]

for _ in range(28):
    come = int(input())
    student.remove(come)
    
print(min(student))
print(max(student))