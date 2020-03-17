word = input("Input a word: ")

world_list = list(word)

result = []

for _ in range(len(world_list)):

    result.append(world_list.pop())

# print(result)
print("".join(result))

print(result[::-1])

# Stack Example