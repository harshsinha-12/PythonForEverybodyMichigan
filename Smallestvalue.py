smallest_so_far = None
for i in [9 , 41, 12, 3, 74, 15]:
    if smallest_so_far is None:
        smallest_so_far = i
    elif i < smallest_so_far:
        smallest_so_far = i
    print(smallest_so_far, i)
print(smallest_so_far)
