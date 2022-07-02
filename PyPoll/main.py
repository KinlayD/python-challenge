# dependencies
import csv
from platform import libc_ver

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









    





        

