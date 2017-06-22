def solution(list1, list2):
    result = False
    for x in list1:
        if x in list2:
            result = True
    return result
