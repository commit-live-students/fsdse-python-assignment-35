list1=[1,2,3,4,5]
list2=[2,3,7,3]
def solution(list1,list2):
    res = False
    for i in list1:
        for j in list2:
            if i == j:
                res = True
    return res
solution(list1,list2)    
