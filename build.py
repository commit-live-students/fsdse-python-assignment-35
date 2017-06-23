def solution(list1, list2):
    result = False
    set_a = set(list1)
    set_b = set(list2)
    if( set_a & set_b != set([])):
        result = True
    return result
