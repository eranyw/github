"""
this function is splitng by value of the sex if the sex is male or feamle

"""
def split_male_female(data_set):
    male_dict = {}
    female_dict = {}
    for key, value in data_set.items():
        if data_set[key]["sex"] == "male":
            male_dict[key]=value
    for key,value in data_set.items() :
        if data_set[key]["sex"] == "female":
            female_dict[key] = value
    return male_dict,female_dict

def return_ages (dict):
    ages = []
    for value in dict.values():
        ages.append(value["age"])
    return ages
#finding the mediam average by dviding the sum ages to their length
def find_median_average(dict):

    ages = return_ages(dict)  # use same list for median
    average = sum(ages) / len(ages)
    return average
#printing by age
def  print_values_above( dict, num = None ):
    if num:
        for value in dict.values():
            if value["age"] > num:
                print(value)
    else:
        print(dict.values())

def __main__():
 if __name__ == "__main__":

    data_set = {
        1: {"name": "Tal", "sex": "male", "age": 22},
        2: {"sex": "female", "age": 57, "ID": 17686401, "name": "Anat"},}
    return data_set

    #__main__()
    split_male_female(data_set)
    find_median_average(data_set)
    print_values_above(data_set)
    print_values_above(data_set,55)
