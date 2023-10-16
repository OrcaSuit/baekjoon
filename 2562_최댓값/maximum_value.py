import sys

maxNum = 0
index = 0

for i in range(1,10):
    value = int(sys.stdin.readline().strip()) #ENUMERATE TKDYD
    
    if value > maxNum:
        maxNum = value
        index = i

print(maxNum)
print(index)