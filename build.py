def solution(list1, list2):
    result = False
    '''
    Enter your code here
    '''
    for item in list1:
        if item in list2:
            result = True

    return result
