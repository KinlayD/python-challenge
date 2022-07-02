# dependencies
import csv

# create a variable to count total votes
total_votes = 0
khan = []
correy = []
li = []
o_tooley = []

# open the file and read
filepath_election_data = "../Resources/election_data.csv"
with open(filepath_election_data) as file_election_data:
    reader = csv.reader(file_election_data)

# skip header
    header = next(reader)

    for row in reader:
        total_votes = total_votes + 1
        if row[2] == "Khan":
            khan.append(row)
        if row[2] == "Correy":
            correy.append(row)
        if row[2] == "Li":
            li.append(row)
        if row[2] == "O'Tooley":
            o_tooley.append(row)

# store total number of votes for each candidate
khan_v = len(khan)
correy_v = len(correy)
li_v = len(li)
o_tooley_v = len(o_tooley)

# find percentage of votes for each candidate
khan_p = round((khan_v/total_votes) * 100)
correy_p = round((correy_v/total_votes) * 100)
li_p = round((li_v/total_votes) * 100)
o_tooley_p = round((o_tooley_v/total_votes) * 100)

# find the winner of the election
candidate_votes = (khan_v, correy_v, li_v, o_tooley_v)
candidate_winner_votes = max(candidate_votes)

candidates = ("Khan", "Correy", "Li", "O'Tooley")

candidate_vote_index = candidate_votes.index(candidate_winner_votes)
candidate_winner = candidates[candidate_vote_index]


print("Total Votes")
print(total_votes)
print("-------------------")
print("Khan")
print(khan_v)
print(khan_p)
print("-------------------")
print("Correy")
print(correy_v)
print(correy_p)
print("-------------------")
print("Li")
print(li_v)
print(li_p)
print("-------------------")
print("O'Tooley")
print(o_tooley_v)
print(o_tooley_p)
print("Winner of the election")
print(candidate_winner)
print("-------------------")

# export as .txt 
with open("PyPoll_Analysis.txt", "w") as PyPoll_Analysis:
    PyPoll_Analysis.writelines("Election Results\n")
    PyPoll_Analysis.writelines("------------------------\n")
    PyPoll_Analysis.writelines(f"Total Votes: {total_votes}\n")
    PyPoll_Analysis.writelines("------------------------\n")
    PyPoll_Analysis.writelines(f"Khan: {khan_p}% ({khan_v})\n")
    PyPoll_Analysis.writelines(f"Correy: {correy_p}% ({correy_v})\n")
    PyPoll_Analysis.writelines(f"Li: {li_p}% ({li_v})\n")
    PyPoll_Analysis.writelines(f"O'Tooley: {o_tooley_p}% ({o_tooley_v})\n")
    PyPoll_Analysis.writelines("------------------------\n")
    PyPoll_Analysis.writelines(f"Winner: {candidate_winner}\n")
    PyPoll_Analysis.writelines("------------------------\n")
