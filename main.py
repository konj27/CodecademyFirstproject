import csv
import math

ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []


def sort_out_cols(col_name, lst):
    with open("insurance.csv") as data:
        data_dictionary = csv.DictReader(data)
        for row in data_dictionary:
            lst.append(row[col_name])
    return lst


sort_out_cols("age", ages)
sort_out_cols("sex", sexes)
sort_out_cols("bmi", bmis)
sort_out_cols("children", num_children)
sort_out_cols("smoker", smoker_statuses)
sort_out_cols("region", regions)
sort_out_cols("charges", insurance_charges)
num_ages = [int(i) for i in ages]
print(sum(num_ages)/len(num_ages))
