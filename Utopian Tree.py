def utopianTree(n):
    height = 2**((n // 2) + 1) - 1
    return height if n % 2 == 0 else height*2
