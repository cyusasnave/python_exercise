camelCaseInput = input("Type word using camelCase notation: ")

def camel_to_snake(input):
    chars = list(input)
    transformed_char = []

    for char in chars:
        if char.isupper():
            transformed_char.append("_")
            transformed_char.append(char.lower()) 
        else:
            transformed_char.append(char)
    
    return "".join(transformed_char)

print(camel_to_snake(camelCaseInput))