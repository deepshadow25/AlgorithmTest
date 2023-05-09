n = int(input())

line, end = 0, 0
while n > end:
    line += 1
    end += line
    
diff = end - n
if line%2 != 0:
    top = diff + 1
    bottom = line - diff
else:
    top = line - diff
    bottom = diff + 1

print(f"{top}/{bottom}")