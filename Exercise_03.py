def to_dict(input_string):
    input_dict = {}

    for char in input_string:
        if char.isalpha() and not char.isspace():
            # Convert the letter to lowercase
            lowercase_char = char.lower()

            # Update the count in the dictionary
            input_dict[lowercase_char] = input_dict.get(lowercase_char, 0) + 1

    return input_dict


user_input = input("Enter a string: ")
input_dict = to_dict(user_input)
print("Letter Counts:", input_dict)
