def solution(list1, list2):
    result = False
    '''
    Enter your code here
    '''
    for i in list1:
        if i in list2:
            result = True
            break
    return result
