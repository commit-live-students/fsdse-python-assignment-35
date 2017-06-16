def solution(list1, list2):
    result = False
    s1 = set(list1)
    s2 = set(list2)
    result = bool(s1.intersection(s2))
    return result
