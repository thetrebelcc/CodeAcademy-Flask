def max_key(my_dictionary):
    largest_key = float("-inf")
    largest_value = float("-inf")
    for key, value in my_dictionary.items():
        if value > largest_value:
           largest_value = value
           largest_key = key
    return largest_key

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:499999, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"


#function that takes in dict 
# take in largest key and value
#for loop that takes the values and find the biggest, with the corresponding key. 
#return the key 