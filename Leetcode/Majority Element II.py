from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        if len(nums) < 3:
            return (list(set(nums)))
        else:     
            counter = Counter(nums)
            treshhold = len(nums) // 3
            return [key for key,val in counter.items() if val > treshhold]
        
# runtime 86 ms Beats 97.99% of users with Python3
# space 17.86mg Beats 78.71% of users with Python3
        



#? space optimized answer1 
# def majorityElement(nums: List[int]) -> List[int]:
#     treshold = len(nums) / 3
#     return [n for n, c in Counter(nums).items() if c > treshold]
# with open('user.out', 'w') as f:
#     for case in map(loads, stdin):
#         f.write(f"{majorityElement(case)}\n")
#     exit(0)


#? space opimized answer2
# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
    
#         dct = {}
#         sol = []
#         n = len(nums)
#         for no in nums:
#             if(no in dct.keys()):
#                 dct[no]+=1
#             else:
#                 dct[no]=1
#             if(dct[no]==n//3+1):
#                 sol.append(no)
        
#         return(sol)



#? runtime optimized answer1
# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         x = y = None
#         cx = cy = 0

#         for num in nums:
#             if cx == 0 and num != y:
#                 x = num
#                 cx = 1
#             elif cy == 0 and num != x:
#                 y = num
#                 cy = 1
#             elif num == x:
#                 cx += 1
#             elif num == y:
#                 cy += 1
#             else:
#                 cx -= 1
#                 cy -= 1

#         cx = cy = 0
#         for num in nums:
#             if num == x:
#                 cx += 1
#             elif num == y:
#                 cy += 1

#         result = []
#         if cx > len(nums) // 3:
#             result.append(x)
#         if cy > len(nums) // 3:
#             result.append(y)
#         return result        