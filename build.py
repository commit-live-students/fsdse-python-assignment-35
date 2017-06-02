def solution(list1, list2):
    result = False
    '''
    Enter your code here
    '''
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                return True
    return False
