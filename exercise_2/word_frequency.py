input_value = input("Write a sentence:")

def word_dictionary(value):
    list_of_words = value.split(" ")
    my_dictionary = {}

    for item in list_of_words:
        if (item in my_dictionary.keys()):
            my_dictionary[item] += 1
        else:
            my_dictionary[item] = 1
    
    print(my_dictionary)

word_dictionary(input_value)