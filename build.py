def solution(list1, list2):

    for i in range (0,len(list1)):
        for j in range (0, len(list2)):
            if list1[i] == list2[j]:
                return True
    else:
        return False


'''
a = [1,2,3,4,5]
b = [5,6,7,8]
print solution(a,b)
'''
