import random

def bubble_sort(lst):
	for i in range(0,len(lst)-1):
	    for j in range(0,len(lst)-1-i):
	        if lst[j] > lst[j+1]:
	            list_swap(lst,j,j+1)

	return lst


def list_swap(lst,x,y):
    z = lst[y]
    lst[y] = lst[x]
    lst[x] = z

list=[]
for i in range(0,100):
    list.append(random.randint(1,100))

print('the original list is:')
print(list)

print('---------------')
print('the list sorted is:')
print(bubble_sort(list))