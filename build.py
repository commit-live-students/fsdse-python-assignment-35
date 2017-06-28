def solution(list1, list2):
    result = False
    '''
    Enter your code here
    '''
    set1 = set(list1)
    set2 = set(list2)

    if len(set1.intersection(set2)) > 0:
        return True
    return False
