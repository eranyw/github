import pytest
import logging

#getting by value key for man and female
#@pytest.Mark.smoke
@pytest.mark.xfail(raises=IndexError)
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

#@pytest.Mark.regression
#getting ages oof the man and woman
def return_ages (dict):
    ages = []
    for value in dict.values():
        ages.append(value["age"])
    return ages
#median calacute by dviding sum ages and the ken ages
def find_median_average(dict):
 ages = return_ages(dict)  # use same list for median
 average = sum(ages) / len(ages)
 return average



def  print_values_above( dict, num = None ):
    if num:
        for value in dict.values():
           if value["age"] > num:
               print(value)
    else:
               print(dict.values())


data_set = {
1: {"name": "Tal", "sex": "male", "age": 22},
2: {"sex": "female", "age": 57, "ID": 17686401, "name": "Anat"},}



split_male_female(data_set)
find_median_average(data_set)
print_values_above(data_set)
print_values_above(data_set, 55)









LOGGER = logging.getLogger(__name__)


def test_log():
    LOGGER.info('info')
    LOGGER.warning('warning')
    LOGGER.error(' error')
    LOGGER.critical('critical')
    assert True
