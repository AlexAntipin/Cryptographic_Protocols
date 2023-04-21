l = [7, 10, 9, 8, 6]
print(all(l[i] >= l[i+1] for i in range(len(l) - 1)))
