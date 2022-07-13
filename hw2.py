s = "dabaxyddab"
dict = {"b": 2, "d": 3, "a": 3, "x": 1, "y": 1}
for i in s:
    dict[i] = dict.get(i,0)+1

sorted_dict = {key: value for key, value in sorted(dict.items())}
print(sorted_dict)

value_dict = sorted([(value, key) for (key, value) in dict.items()])
print(value_dict)

st1 = [11,  7, 5,  8, 5,  37,  11, 5]
lst2 = [22, 8, 10, 1, 11]
lsr3 = [ 71, 3, 22, 8, 2, 14, 1]


set1 = set(st1)
set2 = set(lst2)
set3 = set(lsr3)
if len(st1)-len(set1) >0:
    print("this is a repeted list")

    repeted = {x for x in st1 if st1.count(x) > 1}
    print(repeted)
else:
    print("there is no repeted list")
if len(lst2)-len(set2) >0:
    print("this is a repeted list")
else:
    print("there is no repeted list")
if len(lsr3)-len(set3) >0:
    print("this is a repeted list")
else:
    print("there is no repeted list")


print(len(st1)-len(set1))
set_res1 = set1.intersection(set2)
set_res2 = set_res1.intersection(set2)
final_list = list(set_res2)
print(final_list)

lst = [31, 99, 3, 1943,0]
sort_order_asc =[]


sort_order_asc = []
for i in lst:
    while i >= 10:
        sort_order_asc.append(i%10)
        i = i//10
    sort_order_asc.append(i)

sort_order_asc=set(sort_order_asc)
print(sort_order_asc)
sort_order_desc=list(sort_order_asc)

sort_order_desc =sort_order_desc[::-1]
print(sort_order_desc)
