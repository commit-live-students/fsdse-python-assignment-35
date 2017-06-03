def solution(list1, list2):
    result = False
    if len(list(filter(lambda x: x in list1,list2)))>0:
        result=True
    return result
