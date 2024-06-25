# Implementation of Find S algorithm
import pandas as pd

# Data from the provided CSV file
data = {
    "Sky": ["Sunny", "Sunny", "Rainy", "Sunny"],
    "AirTemp": ["Warm", "Warm", "Cold", "Warm"],
    "Humidity": ["Normal", "High", "High", "High"],
    "Wind": ["Strong", "Strong", "Strong", "Strong"],
    "Water": ["Warm", "Warm", "Warm", "Cool"],
    "Forecast": ["Same", "Same", "Change", "Change"],
    "EnjoySport": ["Yes", "Yes", "No", "Yes"]
}

df = pd.DataFrame(data)

file_path = '/Users/supreettembadmani/Desktop/enjoysport.csv'

df.to_csv(file_path, index=False)

print(f"CSV file has been created at {file_path}")

import csv

# Read the data from the CSV file
a = []
with open(file_path, 'r') as csvfile:
    next(csvfile)  # Skip the header row
    for row in csv.reader(csvfile):
        a.append(row)

print(a)
print("\nThe total number of training instances are: ", len(a))

# Determine the number of attributes
num_attribute = len(a[0]) - 1

# Initialize the hypothesis
print("\nThe initial hypothesis is:")
hypothesis = ['0'] * num_attribute
print(hypothesis)

# Iterate over each instance in the dataset
for i in range(len(a)):
    if a[i][num_attribute] == 'yes':
        print("\nInstance", i + 1, "is", a[i], "and is a Positive Instance")
        for j in range(num_attribute):
            if hypothesis[j] == '0' or hypothesis[j] == a[i][j]:
                hypothesis[j] = a[i][j]
            else:
                hypothesis[j] = '?'
        print("The hypothesis for the training instance", i + 1, "is:", hypothesis, "\n")
    if a[i][num_attribute] == 'no':
        print("\nInstance", i + 1, "is", a[i], "and is a Negative Instance Hence Ignored")
        print("The hypothesis for the training instance", i + 1, "is:", hypothesis, "\n")

print("\nThe Maximally specific hypothesis for the training instance is", hypothesis)