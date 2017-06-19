def solution(list1, list2):
    result = False
    '''
    Enter your code here
    '''
    for x in list1:
        if x in list2:
            result = True
            return result
    return result
