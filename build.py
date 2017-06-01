def solution(list1, list2):
    result = False
    for i in range(0,len(list1)):
        for j in range(0,len(list2)):
            if list1[i] == list2[j]:
                result = True
            j = 0
    return result
