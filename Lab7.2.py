sp = []
sp.append(input('Введіть рядок  '))
sp.append(input('Введіть рядок  '))
sp.append(input('Введіть рядок  '))
sp.append(input('Введіть рядок  '))
sp.append(input('Введіть рядок  '))
newsp = []
mainsp = []
for i in range(0, len(sp)):
    foo = int(len(sp[i])/2)
    bar = sp[i][int(len(sp[i])/2)].capitalize()
    newsp.append(sp[i].replace(sp[i][foo], bar))
for j in range(0, len(newsp)):
    foo1 = int((len(newsp[j])/2)-1)
    bar1 = newsp[j][int((len(newsp[j])/2)-1)].capitalize()
    mainsp.append(newsp[j].replace(newsp[j][foo1], bar1))
print(' '.join(mainsp))