def unique_elements(input_list):
    ourSet = set()

    for element in input_list:
        ourSet.add(element)

    ourList = list(ourSet)
    return ourList


test_list = [3, 7, 5, 1, 0, 3, 9, 0, 0, 0, 5, 1]
result = unique_elements(test_list)
print("Original List:", test_list)
print("List with Unique Elements:", result)