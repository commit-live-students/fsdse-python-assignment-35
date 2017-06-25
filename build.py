def solution(list1, list2):
    result = False
    for i in list1:
        for j in list2:
            if (i == j):
                result = True
                return result
    return result
