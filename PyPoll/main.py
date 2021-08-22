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
    
  vote_percentage = round((value/total_votes) * 100,2)
    
  
  print(key + ":" + str(vote_percentage) + "," + str(value))
  

print("Total Votes:" + str(total_votes))
  
  

print('\nMost Votes:')

print(most_candidate_name + ": " + str(most_votes_count))

