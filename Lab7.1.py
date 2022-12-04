s = input('Введіть рядок  ')
s1 = s.split(' ')
sp = []
for i in s1:
    sp.append((len(i), i))
sp.sort()
print(sp[-1], 'кількість слів = ' + str(len(sp)))