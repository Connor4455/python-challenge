import os
import csv

election_data = os.path.join("..","Resources","election_data.csv")

with open(election_data, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)
    data = list(csvreader)
    rows = len(data)

    candidate_list = list()
    tally = list()
    for i in range (0,rows):
        candidate = data[i][2]
        tally.append(candidate)
        if candidate not in candidate_list: 
            candidate_list.append(candidate)
    candidate_count = len(candidate_list)

    votes = list()
    percentage = list()
    for j in range (0,candidate_count):
        name = candidate_list[j]
        votes.append(tally.count(name))
        vote_percent = votes[j]/rows
        percentage.append(vote_percent)

    winner = votes.index(max(votes))    

    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {rows:,}")
    print("----------------------------")
    for k in range (0,candidate_count): 
        print(f"{candidate_list[k]}: {percentage[k]:.3%} ({votes[k]:,})")
    print("----------------------------")
    print(f"Winner: {candidate_list[winner]}")
    print("----------------------------")

output_file = os.path.join("..", "Analysis", "analysis.md")

with open(output_file,"w") as file:

    file.write("Election Results")
    file.write("----------------------------")
    file.write(f"Total Votes: {rows:,}")
    file.write("----------------------------")
    for k in range (0,candidate_count): 
        file.write(f"{candidate_list[k]}: {percentage[k]:.3%} ({votes[k]:,})")
    file.write("----------------------------")
    file.write(f"Winner: {candidate_list[winner]}")
    file.write("----------------------------")