def solution(list1, list2):
    result = False
    # a = [1,2,3,4]
    # b = [5,6,7,8]
    count = 0

    for elem_a in list1:
        for elem_b in list2:
            if elem_a == elem_b:
                count += 1
        # print count
    if (count == 1):
        result = True
    else:
        result
    return result
