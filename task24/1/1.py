f = open('24.txt')
line = f.readline().strip()
max_len = 0
cur_len = 0
for i in range(len(line)):
    if line[i] == 'Y':
        cur_len += 1
    else:
        cur_len = 0
    if cur_len > max_len:
        max_len = cur_len
print(max_len)