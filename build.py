def solution(list1, list2):
    c=[]
    for i in list1:
        if i in list2:
            c.append(True)
        else:
            c.append(False)
    if True in c:
        result= True
    else:
        result=False
    return result
