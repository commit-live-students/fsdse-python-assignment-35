def solution(list1, list2):
    result = False
    if len(set(list1) & set(list2)) > 0:
        result = True
    return result
