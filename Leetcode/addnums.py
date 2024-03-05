# import itertools
# # def best_practice(n:list,target:int):
# #     itertools.accumulate

# nlist = [0,3,2,4,0]
# target = 8
# nlist.sort()
# new_list = [x for x in nlist if x <= target]
# r = itertools.accumulate([1,2,3,4])
# ri = itertools.combinations(new_list, 2)
# items = []
# # for i in ri:
# #     if i[0] + i[1] == target and i[0] != i[1]:
# #         items.append(new_list.index(i[0]))
# #         items.append(new_list.index(i[1]))
# #         print(items)
# #         print("x")
# #     elif i[0] == i[1]:
# #         items.append(new_list.index(i[0]))
# #         ne = new_list.index(i[0])
# #         new_list[ne] = "X"
# #         items.append(new_list.index(i[1]))        
# #         print(items)

# for i in ri:
#     print(i)

e = [
2,5,3
]

r = [5,90]

e.extend(r)
print(e)
if len(e) % 2 != 0:
    d = e[len(e) // 2]
    print((float(d)))
else:
    t = len(e) // 2
    ans = (e[t] + e[t-1]) / 2
    print(ans)
# print(d)
# print(e)

# t = len(r) // 2
# print(r[t])