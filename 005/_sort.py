def sort_(ls):
    """
    It sorts a sequence and return new list one.
    """
    l = ls.copy()
    for _ in range(len(l)):
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

    return l


list_ = [7, 4, 2, -4, 1]
print(sort_(list_))
