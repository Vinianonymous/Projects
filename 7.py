a = ['b', 'waaa', 'nao', 'vida', 'barco', 'icoti', 'joao', 'aviao', 'oxigenio', 'dez']
b = ['ronaldo', 'victor', 'heitor', 'figado', 'coracao']
c = []

i = 0
while i < len(a):
    c.append(a[i])
    if i < len(b):
        c.append(b[i])
    i +=1
print(c)

#Ordenar alfabeticamente de z à a

for i in range(len(c)):
    for j in range(len(c)):
        if c[i] > c[j]:
            x = c[i]
            c[i] = c[j]
            c[j] = x

print(c)
