def add(a, b):
  c = a + b
  return c

print(add(3,4))

def add(a, b = 4):
  c = a + b
  return c

print(add(4))

def add(a, b, c):
  d = a + b + c
  print(d)

e = (1, 20, 3)
add(*e)

a = 123

def setGlobal():
  global a
  a = 456
  print("Global:", a)

setGlobal()
print("Global:", a)
