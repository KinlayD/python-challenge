# dependencies
import os
import csv

# file path
input_file = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidate = []



# Read csv file
with open(input_file) as file:
    reader = csv.reader(file, delimiter =",")

    headers = next(reader)

    first_row = next(reader)
    total_votes = total_votes + 1
    votes = first_row[2]

    for row in reader:
        total_votes = total_votes + 1
        vote_count = votes + [row[2]]
        candidate.append(vote_count)
        candidate_names = ["Khan", "Correy", "Li", "O'Tooley"]
        candidate_dict = dict.fromkeys(candidate_names, candidate) 
        
        
        khan = [khan.append for x in candidate_dict if x == "Khan"]
        correy = [correy.append for x in candidate_dict if x == "Correy"]
        li = [li.append for x in candidate_dict if x == "Li"]
        o_tooley = [o_tooley.append for x in candidate_dict if x == "O'Tooley"]
            
total_khan = len(khan)
khan_percent_vote = total_khan/total_votes * 100
total_correy = len(correy)
correy_percent_vote = total_correy/total_votes * 100
total_li = len(li)
li_percent_vote = total_li/total_votes * 100
total_o_tooley = len(o_tooley)
o_tooley_percent_vote = total_o_tooley/total_votes * 100


print("Election Results")
print("---------------------------")
print(f'Total Votes: {total_votes}')
print("---------------------------")
print(f'{candidate_names[0]}: {khan_percent_vote}% ({total_khan})')
print(f'{candidate_names[1]}: {correy_percent_vote}% ({total_correy})')
print(f'{candidate_names[2]}: {li_percent_vote}% ({total_li})')
print(f'{candidate_names[3]}: {o_tooley_percent_vote}% ({total_o_tooley})')












    





        

