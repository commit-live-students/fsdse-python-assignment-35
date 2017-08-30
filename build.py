def solution(list1, list2):
    result = False
    '''
    Enter your code here
    '''
    for x in list1:
        for y in list2:
            if x == y:
                result = True
    return result
