def selection_sort(list):
    """ This is Selection Sort function """
    """we just have to find min in list and swap it"""

    print(f"List Before Sort : {list}")

    for i in range(len(list)):
        index = i
        for j in range(i, len(list)):
            if list[j] < list[index]:
                list[index], list[j] = list[j], list[index]
    print(f"List After Sort : {list}")


l1 = [60, 16, 80, 57, 22, 67, 69, 63, 9, 48, 62, 5, 99, 56, 50, 11, 73, 59, 15, 13, 39, 94, 28, 85]

selection_sort(l1)