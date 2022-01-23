# 3.4.5 Module 3
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Desktop","DataAnalyticsBootcamp","03-Python","election-analysis","Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Desktop","DataAnalyticsBootcamp","03-Python","election-analysis","analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)


    