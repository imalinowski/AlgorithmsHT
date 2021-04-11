from typing import List


def anti_quick_sort(array: List[int]):
    for i in range(1, n):
        array[i], array[int(i / 2)] = array[int(i / 2)], array[i]

with open('input.txt') as file:
    n = int(file.readline())
array = [x for x in range(1, n + 1)]
anti_quick_sort(array)

f = open("output.txt",'w')
for x in array:
    f.write(str(x)+' ')
print("answer was written in output.txt") 
