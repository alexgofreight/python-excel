variable_a = 5.0
variable_b = variable_a + 5
print(variable_b)
print(type(variable_b))

list_a = [variable_a, variable_b, 'Alex']
print(list_a)

c = 10
d = 3
print(c % d)
print(2 ** 4)
print(9 // 3)
print(c // d)

variable_c = int(7.2)
print(variable_c)
variable_d = str(7.2)
print((variable_d))

dict_a = {"key": "value", "fruit": "apple"}
print(dict_a["fruit"])

xx = 5
yy = 8
if xx > yy:
  print('Hi')
else:
  print('Yo')

list_x = [1,2,3,4,5]
for item in list_x:
  print(item)

ii = 1
while ii < 10:
  print(ii)
  ii = ii + 1

# Function
def add_two(number):
  number = number + 2
  return number

print(add_two(4))

abc = 'string'
print(dir(abc))
print(abc.upper())

