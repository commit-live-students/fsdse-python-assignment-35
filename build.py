def solution(list1, list2):
    result = False
    set1 = set(list1)
    set2 = set(list2)
    if(len(set1.intersection(set2))>0):
        result = True
    return  result

solution([1,2,3,4],[4,5,6,7])
