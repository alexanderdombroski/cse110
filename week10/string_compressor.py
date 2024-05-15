print('Welcome to the string compressor using huffman tree')
starter_string = input("Type a string you would like to compress: ")

values_dictionary = {}
for letter in starter_string:
    values_dictionary[letter] = values_dictionary.get(letter, 0) + 1

items_list = list(values_dictionary.items())

items_list = sorted(items_list, key=lambda x: x[1], reverse= True)

print(items_list)


tree_code = {}
for index in range(len(values_dictionary.keys())):
    print(f"{items_list[index][0]}, {items_list[index][1]}, {index}")
    
    tree_code[items_list[index][0]] = items_list[index][1]
    # Need to add a system to assign binary paths to a list