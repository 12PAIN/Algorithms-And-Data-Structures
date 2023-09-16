import timeit as timeit
import matplotlib.pyplot as plt
import numpy as np
import random as rnd

x = [100, 200 ,1000, 2000]
time_arr_1_1 = []
time_arr_1_2 = []
time_arr_1_3 = []

time_arr_2_1 = []
time_arr_2_2 = []
time_arr_2_3 = []

def myFastSort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = rnd.choice(nums)
   l_nums = [n for n in nums if n < q]
 
   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return myFastSort(l_nums) + e_nums + myFastSort(b_nums)
   
def mySelectSort(alist):
    for i in range(0, len(alist) - 1):
        smallest = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]

for i in x:
    arr_1 = [rnd.randint(-100,100) for j in range(1,i)]
    arr_2 = [rnd.randint(-100,100) for j in range(1,i)]
    time_arr_1_1.append(timeit.timeit("myFastSort(arr_1)", number=1, globals=globals()))
    time_arr_2_1.append(timeit.timeit("mySelectSort(arr_2)", number=1, globals=globals()))
    
    arr_1 = myFastSort(arr_1)
    mySelectSort(arr_2)
    
    time_arr_1_2.append(timeit.timeit("myFastSort(arr_1)", number=1, globals=globals()))
    time_arr_2_2.append(timeit.timeit("mySelectSort(arr_2)", number=1, globals=globals()))
    
    arr_1.sort(reverse=True)
    arr_2.sort(reverse=True)
    
    time_arr_1_3.append(timeit.timeit("myFastSort(arr_1)", number=1, globals=globals()))
    time_arr_2_3.append(timeit.timeit("mySelectSort(arr_1)", number=1, globals=globals()))
    
fig = plt.figure()
print (fig.axes)  
print (type(fig)) 

plt.plot(x, time_arr_1_1, color="red");
plt.plot(x, time_arr_1_2, color="red");
plt.plot(x, time_arr_1_3, color="red");

#plt.plot(x, time_arr_2_1, color="green");
#plt.plot(x, time_arr_2_2, color="blue");
#plt.plot(x, time_arr_2_3, color="yellow");

plt.ylabel("Time")
plt.xlabel("Elements")

print (fig.axes)

plt.show()
      

    