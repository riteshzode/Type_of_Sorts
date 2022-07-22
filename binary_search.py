def binary_search(list, no):
    """ This is binary search function """
    l = 0
    u = len(list) - 1


    while l <= u:

        mid = (l + u) // 2

        if list[mid] == no:
            print(f"We got the no at index no at {mid}")
            return True
        else:
            if list[mid] < no:
                l = mid + 1
            else:
                u = mid - 1
    return False


l1 = [5, 9, 11, 13, 15, 16, 22, 28, 39, 48, 50, 56, 57, 59, 60, 62, 63, 67, 69, 73, 80, 85, 94, 99]


n = 594

if binary_search(l1, n):
    print("Found")
else:
    print('Not Found, the number not Exists')
