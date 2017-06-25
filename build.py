def solution(list1, list2):
    result = False
    for value_1 in list1:
        for value_2 in list2:
            if value_1 == value_2:
                result = True
                break
    return result
