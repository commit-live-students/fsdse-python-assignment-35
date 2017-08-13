def solution(list1, list2):
    result = False
    result = True if set(list1) & set(list2) else False
    return result
