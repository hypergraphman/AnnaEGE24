from itertools import permutations

words = [''.join(word) for word in permutations('тимур', r=4)]
print(len(words))
k = 0
for word in words:
    t = word.replace('т', '+').replace('и', '-').replace('м', '+').replace('у', '-').replace('р', '+')
    if t in ('+-+-', '-+-+'):
        k += 1
print(k)