import random

#通过比较-插入方式将一个列表排序，最小的在前面
def insert_sort(lst):
	for i in range(1, len(lst)):
		temp = lst[i]
		j = i - 1
		while j >= 0 and temp < lst[j]:
			lst[j + 1] = lst[j]
			j -= 1
		lst[j + 1] = temp
	return lst



list=[]
for i in range(0,100):
    list.append(random.randint(1,100))

print('the original list is:')
print(list)

print('---------------')
print('the list sorted is:')
print(insert_sort(list))