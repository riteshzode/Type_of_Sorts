def bubble_sort(list):
    """ This is Bubble Sort function """

    print(f"List Before Sort : {list}")

    for i in range(len(list) - 1, 0, -1):

        for j in range(i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    print(f"List After Sort : {list}")



l1 = [60, 16, 80, 57, 22, 67, 69, 63, 9, 48, 62, 5, 99, 56, 50, 11, 73, 59, 15, 13, 39, 94, 28, 85]

bubble_sort(l1)