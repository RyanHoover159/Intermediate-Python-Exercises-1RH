def combine_dicts(dict_1, dict_2):
    combined_dict = {}
    for key in set(dict_1.keys()) & set(dict_2.keys()):
        combined_dict[key] = dict_1[key] + dict_2[key]

    return combined_dict


dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"b": 4, "a": 3, "d": 9, "c": 5}
comnined_dict = combine_dicts(dict_1, dict_2)

print("Combined Dictionary:", comnined_dict)