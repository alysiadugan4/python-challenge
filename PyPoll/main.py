import csv
import os

votes = {}

total_votes = 0
most_votes_count = 0
most_voted_candidate = ""



with open('Resources\election_data.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    for row in csvreader:

      candidate_name = row[2]

      total_votes = total_votes + 1

      if candidate_name in votes:
        votes[candidate_name] = votes[candidate_name] + 1
      else:
        votes[candidate_name] = 1


    
for key, value in votes.items():

  if value > most_votes_count:
    most_candidate_name = key
    most_votes_count = value
    
  vote_percentage = (value/total_votes)
    
  
  print(key + ":" + "{:.2%}".format(vote_percentage) + ";" + "{:,}".format(value))
  

print("Total Votes:" + "{:,}".format(total_votes))
  
  

print('Winner:')

print(most_candidate_name + ": " + "{:,}".format(most_votes_count))

file_name = "PyPoll.txt"

with open(file_name,'w') as txt_file:
    txt_file.write("Voting Results\n")
    txt_file.write("--------------------\n")
    txt_file.write("Total Votes:" + "{:,}".format(total_votes) + "\n")
    txt_file.write("--------------------\n")
    txt_file.write(key + ":" + "{:.2%}".format(vote_percentage) + ";" + "{:,}".format(value) + "\n")
    txt_file.write("--------------------\n")
    txt_file.write('Winner:\n')
    txt_file.write(most_candidate_name + ": " + "{:,}".format(most_votes_count))
