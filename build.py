def solution(list1, list2):
    result = False
    '''
    Enter your code here
    '''
    if len(list1) + len(list2) > len(set(list1+list2)):
        result = True
    else:
        result = False

    return result
