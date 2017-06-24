def solution(list1, list2):
    if set(list1).intersection(list2):
        return True
    else:
        return False

# solution([1,2,3,4,5], [5,6,7,8])
# Output: True

# solution([1,2,3,4,5], [6,7,8,9,0])
#Output : False
