result_search = []
for x in '01234567':
    for y in '01234567':
        t = int(x + '01' + y + '4', 9) + int(x + y + '544', 8)
        if t % 89 == 0:
            result_search.append(t)
if result_search:
    print(min(result_search) // 89)
