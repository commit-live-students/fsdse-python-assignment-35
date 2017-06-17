def solution(list1, list2):
    result = False
    for i in range(len(list1)):
        if( list1[i] in list2):
            return True
    return result
