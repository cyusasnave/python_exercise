my_input = input("Type any word or sentence with vowels: ")
VOWELS = ['a' , 'e' , 'i' , 'o' , 'u' , 'A' , 'E' , 'I' , 'O' , 'U']

def remove_vowels(input):
    chars = list(input)
    transformed_chars = []

    for char in chars:
        if isVowel(char):
            continue
        else:
            transformed_chars.append(char)
    
    return ''.join(transformed_chars)

def isVowel(char):
    if char in VOWELS :
        return True
    else:
        return False
    

print(remove_vowels(my_input))