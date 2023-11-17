#library imports
import csv
import os

#script variables
csv_header = " "
total_votes = 0
candidate_found = False
candidates_dump = []
candidates_list = []
candidates_percentages = []
candidates_votes = []
election_winner = " "

#define the file path and read into reader
csv_path = os.path.join("PyPoll", "Resources", "election_data.csv")
with open(csv_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #read and store csv file header    
    csv_header = next(csv_reader)
    
    #logic control to loop through the csv file
    for row in csv_reader:

    #read candidates into list
        candidates_dump.append(row[2])

    #add votes to total votes
        total_votes = total_votes + 1

    #end loop through csv file

candidates_list.append(candidates_dump[0])
candidates_votes.append(0)

#determine candidate, locate in list (add if not found), and add votes to matching votes list

for x in range(len(candidates_dump)):
    candidate_found = False
    for y in range(len(candidates_list)):
                 
        #check for candidate
        if(candidates_list[y] == candidates_dump[x]):
                #add votes in coresponding votes list
            candidate_index = candidates_list.index(candidates_list[y])
            candidates_votes[candidate_index] = candidates_votes[candidate_index] + 1
            candidate_found = True
    
    if(candidate_found == False):    
        candidates_list.append(candidates_dump[x])
        candidates_votes.append(1)   
            

#determine percentages and read into percentages list
for x in range(len(candidates_votes)):
     candidates_percentages.append(round((candidates_votes[x]/total_votes)*100,2))

#determine overall winner
for x in range(len(candidates_votes)):
     if candidates_votes[x] == max(candidates_votes):
         election_winner = candidates_list[x]

#write to text file and create
filename = 'PyPoll/Analysis/election_analysis.csv'
#fpath = ('PyPoll/Analysis/financial_analysis.csv') not used
with open(filename, 'w') as csvfile:
         csvwriter = csv.writer(csvfile)
         csvwriter.writerow(["Election Analysis"])
         #csvwriter.writerow(" ")
         csvwriter.writerow(["------------------"])
         #csvwriter.writerow(" ")
         csvwriter.writerow(["Total Votes: " + str(total_votes)])
         #csvwriter.writerow(" ")
         for i in range(len(candidates_list)):
           csvwriter.writerow([candidates_list[i] + ": " + str(candidates_percentages[i]) + "%, " + "("+str(candidates_votes[i])+")"])
         #csvwriter.writerow(" ")
         csvwriter.writerow(["------------------"])
         csvwriter.writerow(["Election Winner: " + str(election_winner)])
         #csvwriter.writerow(" ")
         csvwriter.writerow(["------------------"])
#write to text file closes

#print results
print(" ")
print("Election Results")
print(" ")
print("---------------------------")
print(" ")
print("Total Votes: " + str(total_votes))
print(" ")
print("---------------------------")
print("Candidates List: ")
print(" ")
for i in range(len(candidates_list)):
     print(candidates_list[i] + ": " + str(candidates_percentages[i]) + "%, " + "("+str(candidates_votes[i])+")")
print(" ")
print("---------------------------")
print(" ")
print("Winner: " + election_winner)
print("---------------------------")