def solution(list1, list2):
    result = False
    for lValue1 in list1:
        for lValue2 in list2:
            if lValue1 == lValue2:
                result = True
                break
    return result


print solution([1,2,3], [2,3])
