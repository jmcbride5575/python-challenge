# Import dependencies
import os
import csv

#Set path for CSV
election_csv = os.path.join("election_data.csv")

# Set Variables
total_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
Otooley_votes = 0
winner = ["Khan","Correy", "Li", "OTooley"]

# Open/Read CSV File
with open(election_csv, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvfile)
    
    for row in csvreader:
        total_votes = total_votes + 1
        
        if (row[2] == "Khan"):
            Khan_votes += 1
        elif (row[2] == "Correy"):
            Correy_votes +=1
        elif (row[2] == "Li"):
            Li_votes +=1
        else:
            Otooley_votes +=1

# Calculate percentage of win votes for each person
Khan_percent = Khan_votes / total_votes
Correy_percent = Correy_votes / total_votes
Li_percent = Li_votes / total_votes
Otooley_percent = Otooley_votes / total_votes 

winner = max(Khan_votes, Correy_votes, Li_votes, Otooley_votes)

if winner == Khan_votes:
    winner_name = "Khan"
elif winner == Correy_votes:
    winner_name = "Correy"
elif winner == Li_votes:
    winner_name == "Li"
else:
    winner_name == "O'Tooley"

# Analysis
print(f"Election Results")
print (f"-----------------------------")     
print (f" Total Votes: {total_votes}")
print (f" Khan: {Khan_percent:.3%}({Khan_votes})")
print (f" Li: {Li_percent:.3%}({Li_votes})")
print (f" Correy {Correy_percent:.3%}({Correy_votes})")
print (f" Otooley {Otooley_percent:.3%}({Otooley_percent})")       
print (f"-----------------------------")
print (f"Winner: []")

# set file to write text file to
output_file= os.path.join("election_data_completed.text")

#write text data
with open(output_file,'w',)as txtfile:
    txtfile.write(f"Election Results")
    txtfile.write(f"---------------------------")
    txtfile.write(f"Total Votes: {total_votes}")
    txtfile.write(f"---------------------------")
    txtfile.write(f" Khan: {Khan_percent:.3%}({Khan_votes})")
    txtfile.write(f" Li: {Li_percent:.3%}({Li_votes})")
    txtfile.write(f" Correy {Correy_percent:.3%}({Correy_votes})")
    txtfile.write(f" Otooley {Otooley_percent:.3%}({Otooley_percent})")
    txtfile.write(f"-----------------------------")
    print (f"Winner: []")

