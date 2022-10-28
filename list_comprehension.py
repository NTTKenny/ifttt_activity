dic = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
a = [(1, 3)]
for (start, end) in a:
    list_1 = [value for value in list(dic.keys()) if start <= value <= end]
    print(list_1)

 
