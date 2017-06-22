def solution(list1, list2):
#     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return True
     return False
#             else:
#                 result = False
#                 return False
print(solution([1,2,3,4,5], [5,6,7,8]))
print(solution([1,2,3,4], [5,6,7,8]))
