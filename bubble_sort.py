import random
def list_swap(list,x,y):
    z = list[y]
    list[y] = list[x]
    list[x] = z

list=[]
for i in range(0,100):
    list.append(random.randint(1,100))
print(list)

times_of_change = 0
for i in range(0,len(list)-1):
    for j in range(0,len(list)-1-i):
        if list[j] > list[j+1]:
            list_swap(list,j,j+1)
            times_of_change = times_of_change + 1
print(list)
print(times_of_change)
