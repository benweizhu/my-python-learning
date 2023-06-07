import copy
import random


def add(x, y):
    return round(x + y, 2)


def print_string(string):
    print(string)


def print_string_index_char(string, index):
    print(string[index])


print(add(1.23, 2.80))

print_string("呜呜呜")

print_string_index_char("abc", 2)

print("sub_string"[1:3])

print(type(add(1, 2)))

print(type(str(add(2, 3))))

print(random.randint(1, 100))

print(11 == '11')

print(11 != '11')

x = 3

if x == 1:
    print('x is 1')
elif x == 3:
    print('x is 3')
else:
    if x == 2:
        print('x is not 1')
    else:
        print('no')

counter = 1

while counter < 10:
    counter += 1

print(counter)

for word in 'legulegu':
    print(word)

for index in range(10):
    print(index)
logo = "legulegu"
for index in range(len(logo)):
    print(logo[index])

print(logo.upper().lower())

print(logo.startswith("legu"))

print(",".join(["1", "2", "3"]))

print("{} is the website name of legu".format("legulegu"))

some_list = [1, 2, 3, '20']

print('20' in some_list)
print('10' not in some_list)

del some_list[3]

print(some_list)

some_list.remove(1)

print(some_list)

some_list.append(20)

print(some_list)

some_list.insert(1, 1)

print(some_list)

number_list = [6, 3, 6, 7, 9, 3, 32, 2]

number_list.sort(reverse=True)

print(number_list)

print(number_list.index(32))

number_list.pop()

print(number_list)

deepcopy_number_list = copy.deepcopy(number_list)

deepcopy_number_list.append(100)

print(deepcopy_number_list)

my_map = {"key": "value", "key1": "value2"}

print(my_map.keys())
for key in my_map.keys():
    print(key)

print(my_map.values())
for value in my_map.values():
    print(value)

print(my_map.items())
for item in my_map.items():
    print(item)
print(my_map)
print(my_map["key1"])
print(my_map.__contains__("key"))
print("key" in my_map)
print("key3" not in my_map)
print(my_map.get("key1"))
print(my_map.get("key3", "value3notfound"))

set_1 = {1, 2, 3, 4, 5, 5}
print(set_1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
