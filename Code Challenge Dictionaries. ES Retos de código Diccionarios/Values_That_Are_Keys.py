def values_that_are_keys(my_dictionary):  #function 
	value_keys = []                       #dict to hold values
	for value in my_dictionary.values():  #for loop that checks values
		if value in my_dictionary:        # appends if values are in dict
			value_keys.append(value)      
	return value_keys

# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

#Spanish transaltions. 
#función
#diccionario para mantener los valores
# bucle que comprueba valores
#anexa si los valores están en el diccionario

