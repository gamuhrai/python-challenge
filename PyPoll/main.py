# This will allow us to create file path across operating systems
import os

#Module for reading CSV files
import csv

csvpath=os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile: