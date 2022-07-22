def linear_search(list, no):

    for i in range(len(list)):
        if list[i] == no:
            print(f"the position on index no {i}")
            return True


l1 = [5, 3, 8, 6, 7, 2]

n = 23

if linear_search(l1, n):
    print("found")
else:
    print("not found")