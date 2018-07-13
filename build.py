def solution(list1, list2):
    result = False

    if(len(set(list1) & set(list2)) > 0):
        result = True
    return result

print solution([1, 2, 3, 4, 5],[6, 7, 8, 9, 1])
