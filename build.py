def solution(list1, list2):
    return True if ([x for x in list1 if x in list2] or [x for x in list2 if x in list1]) else False
