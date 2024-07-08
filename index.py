def solution(S):
    """
    Returns the minimum number of patches required to repair all the potholes in the road.
    """
    patches = 0
    i = 0
    while i < len(S):
        if S[i] == 'X':
            patches += 1
            i += 3
        else:
            i += 1
    return patches