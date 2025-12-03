my_list = [1, 2, 'a', 'b']

print(my_list)
print(my_list[2])

my_dict = { 'key1': "abc", 'key2': "dfg" }

my_set1 = { 1, 2, 3, 4}
my_set2 = { 4, 5, 6, 7}

if 'key3' in my_dict:
    print('all good')
else:
    print('not good')

name = "Alice"

print("Hello, {1} {0}!".format("sei", name))

print(my_set1)
print(my_set1 | my_set2)
print(my_set1 & my_set2)
print(my_set1 - my_set2)
print(my_set1 ^ my_set2)

for item in my_set1:
    print(item)