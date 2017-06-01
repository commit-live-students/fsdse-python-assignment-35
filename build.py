def solution(list1, list2):
    result = False
    for x in list1:
         for y in list2:
             if x == y:
                 result = True
    return result
output = solution ([5,2,3,4],[1,7,8,9,0])
print output
