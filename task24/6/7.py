f = open('24.txt')
line = f.readline().strip() + '+'
num = ''
max_odd = -1
for i in range(len(line)):
    if line[i] in '0123456789':
        num += line[i]
    else:
        if num and int(num) % 2 != 0 and int(num) >= max_odd:
            max_odd = int(num)
        num = ''
print(max_odd)