#list comprehension
dataset = [4,True,'Dave',2.1,3]
int_data = [num for num in dataset if type(num) == int]
print(int_data)
#prac1
print([i for i in range(1,101)])
print([i for i in range(1,101) if i % 3 == 0])
print([i for i in range(1,101) if i % 7 != 0 and i % 3 != 0])

# set comprehension

int_data = [1,1,2,3,3,4]
square_data_set = {num * num for num in int_data}
print(square_data_set)

# dictionary comprehension

id_name = {1: 'Dave', 2: 'David', 3: 'Anthony'}

print(id_name.items())
# dict_items([(1, 'Dave'), (2, 'David'), (3, 'Anthony')])