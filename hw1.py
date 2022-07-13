# histogram program
# taking a list [3, 7, 2] and useing  repetiton operator
lst = [3,7,2]
i = 0
y = [lst[i] * "*" for i in range(len(lst))]

print(y)


#out put
#histo = ['***', '*******', '**']

"""
2.
#taking two list  by using range
"""
lst1 = ['a', 'b', 'c']
lst2 = ['x', 'y', 'z']
lst_res =[]
i=0
for i in range (len(lst1)):
 LST1=lst1[i]
 LST2=lst2[len(lst1)-1-i]
 lst_res =[LST1+LST2]
 print(lst_res,end="")

#output
# ['az']['by']['cx']



