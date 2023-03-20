#Import Depensencies
import os
import csv

#Declare file path
csv_file_path = ("Resources/election_data.csv")

#Declare variables
total_votes = 0 
Stockham_votes = 0
DeGette_votes = 0
Doane_votes = 0

#Open csv file
with open(csv_file_path,newline="", encoding="utf-8") as elections:

    #create variable to store content
    csvreader = csv.reader(elections,delimiter=",") 
    #Skip header line
    header = next(csvreader)     
    #Iterate trough rows
    for row in csvreader: 
        #Count number of votes and store in total
        total_votes +=1

        #Count the name of each candidate appears   
        if row[2] == "Charles Casper Stockham": 
            Stockham_votes +=1
        elif row[2] == "Diana DeGette":
            DeGette_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            Doane_votes +=1
#create a list for candidates and votes to find the winner        
candidates = ["Stockham", "DeGette", "Doane"]
votes = [Stockham_votes, DeGette_votes, Doane_votes]

#Zip together  the lists being candidates(key) and votes(value) to create a dictionary
dict_candidates_and_votes = dict(zip(candidates,votes))
#Use max function to find the winner
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

#Declare the votes percentage for each candidate
Stockham_percent = (Stockham_votes/total_votes) *100
DeGette_percent = (DeGette_votes/total_votes) * 100
Doane_percent = (Doane_votes/total_votes)* 100


#Print results
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Stockham:{Stockham_percent:.3f}% ({Stockham_votes})")
print(f"DeGette: {DeGette_percent:.3f}% ({DeGette_votes})")
print(f"Doane: {Doane_percent :.3f}% ({Doane_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

#create output file
output_file = ("Resources/Election_Results_Analysis.txt")

#Open output file
with open(output_file,"w") as file:
    #write results for the Analysis.txt
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Stockham: {Stockham_percent:.3f}% ({Stockham_votes})")
    file.write("\n")
    file.write(f"DeGette: {DeGette_percent:.3f}% ({DeGette_votes})")
    file.write("\n")
    file.write(f"Doane: {Doane_percent :.3f}% ({Doane_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")