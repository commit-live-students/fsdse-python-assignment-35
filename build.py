def solution(list1, list2):
    result = False
    for val1 in list1:
        for val2 in list2:
            if val1==val2:
                return True
                break
    return result
print solution([1,2,3,4,5],[5,6,7,8])
