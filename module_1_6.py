my_dict = {"Vasya": 1970, "Petya": 1973, "Dima": 1975}
print(my_dict)
print(my_dict["Petya"])
print(my_dict.get("Venya", 'Такого ключа нет'))
my_dict['Venya'] = 1985
my_dict.update({'Kolya': 1978, 'Vova': 1945})
print(my_dict)
a = my_dict.pop('Dima')
print(my_dict)
print(a)
print(my_dict)
my_set = {1, 2, 3, 8, 15, 2, 13, 'Stop', (1, 2, 3, 8), True}
print(my_set)
my_set.update({324, 855})
print(my_set)
print(my_set.remove(15))
print(my_set)