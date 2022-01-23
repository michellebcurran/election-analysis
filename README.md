# election-analysis
Python Module 3 

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data source: election_results.csv
- Software: Python 3.10.1, Visual Studio Code 1.63.2

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
  -  Charles Casper Stockham
  -  Diana DeGette
  -  Raymon Anthony Doane
- The candidate results were:
  -  Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  -  Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  -  Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
-   Diana DeGette, who received  73.8% of the vote and 272,892 number of votes.

## Challenge Overview - Overview of Election Audit
Employeee needs further election results for Colorado Board of Elections regarding:
  * The voter turnout for each county
  * The percentage of votes from each county out of the total count
  * The county with the highest turnout

Deliverables are as follows:
1. Calculate election results and print to command line.
2. Save election results to a text file.
3. Written analysis of Election Audit (README.md).

## Election Audit Results
- The voter turnout for each county:
  -  Jefferson County received 38,855 votes.
  -  Denver County received 272,892 votes.
  -  Arapahoe County 11,606 votes.
- The percentage of votes from each county out of the total count: 
  - Jefferson County received 10.5% of the vote.
  - Denver County received 82.8% of the vote.
  - Arapahoe County received 3.1% of the vote.
- The county with the highest turnout is Denver.

### Code
Code reference for Election Audit Summary section below.
'''
# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Desktop", "DataAnalyticsBootcamp", "03-Python", "election-analysis", "Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("Desktop", "DataAnalyticsBootcamp", "03-Python", "election-analysis", "analysis", "election_analysis.txt")

'''

## Challenge Summary - Election Audit Summary
In order to use the script for any election, must modify the script as seen above as follows:
- Change file_to_load to a different path that leads to a different csv file. 
i.e. if you have election results from 2017, want to analyze those, and you have saved them in election_results_2017.csv in the same folder then:
    - file_to_load = os.path.join("Desktop", "DataAnalyticsBootcamp", "03-Python", "election-analysis", "Resources", "election_results_2017.csv")
- Change file_to_save to a different path that leads to a different txt file. 
i.e. if you have election results from 2017, want to output the analysis, and want them in election_results_2017.txt in the same folder then:
    - file_to_save = os.path.join("Desktop", "DataAnalyticsBootcamp", "03-Python", "election-analysis", "analysis", "election_analysis_2017.txt")
    
 Therefore, as long as you have a csv file with the data to be analyzed, and a txt file to write or output the results to, then any election can be analyzed using this script.
