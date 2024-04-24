# William Romine
# 00103649
# Dr. Lewis CS472

def is_composite(n):
    if n < 2:
        return True
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return True
    return False