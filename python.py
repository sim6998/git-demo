# dict 


#WORLD
d = {'name':'smit',"age":22}

print(d)

d['salary'] = 20000

print(d)

print('Keys in DIct : ',list(d.keys()))
print('values in Dict : ',list(d.values()))

print('Pair : ',list(d.items()))

l = list(d.values())

d1 = d.fromkeys(l)
print(d1)

# functions

def sum(a,b):
    return a+b

print(sum(5,3))

# List

l = [1,2,3,4,5,6]

l.append(7)
l.remove(2)
print(l)
l.pop(1)
print(l)