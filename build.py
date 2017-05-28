def solution(list1, list2):
    result = False
    '''
    Enter your code here
    '''
    for listValue1 in list1:
        for listValue2 in list2:
            if listValue1 == listValue2:
                result = True
                break
    return result

solution([1,2,3], [2,3])
