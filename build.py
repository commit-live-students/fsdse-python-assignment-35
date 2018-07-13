def solution(list1, list2):
    result = False
    #result = any(i in list1 for i in list2)   #solution one
    return not set(list1).isdisjoint(list2)

list1 = [1,2,3,4]
list2 = [5,6,7,8]

print solution(list1, list2)
