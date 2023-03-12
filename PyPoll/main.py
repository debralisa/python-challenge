#python challenge PyPoll script
<<<<<<< HEAD
#Dependencies
import os
import csv

#from pathlib import Path
#election_data_csv = Path("python-challenge", "PyPoll", "election_data.csv")
election_data_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'election_data.csv')
election_out_txt = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'analysis', 'election_data_out.txt')

#File locations for read and write files
#election_data_csv = "/Users/debralisa3/Dropbox/python-challenge/PyPoll/Resources/election_data.csv"
#election_out_txt = "/Users/debralisa3/Dropbox/python-challenge/PyPoll/Analysis/election_data_out.txt"

#Total vote counter
vote_total = 0

#Candidate options and vote counters
candidate_options = []
candidate_votes = {}

#Winning candidate and winning count trackers
winning_candidate = ""
winning_count = 0

#Read in the csv input file and convert into list of dictionaries
with open(election_data_csv, "r") as election_data:
    reader = csv.DictReader(election_data)

    #For each row
    for row in reader:

        #add to the total vote count and get candidate name per row
        vote_total = vote_total + 1
        candidate_name = row["Candidate"]

        #if condition for no candidate match
        if candidate_name not in candidate_options:

            #append name to the candidate names list and
            #start candidate vote count
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
    
        #then add vote to specific candidate count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#Print results and export data to text file
with open(election_out_txt, "w") as txt_file:

    #Print final results
    election_results = (
        f"\nElection Results\n"
        f"______________________\n"
        f"Total Votes:  {vote_total}\n"
        f"______________________\n"
    )
    print(election_results)

    #save final vote count to file
    txt_file.write(election_results)

    #Calculate the winner with for loop out counts
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes)/float(vote_total) * 100

        #Determine winner and vote count
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        #Print each candidate and voter count
        voter_output = f"{candidate}: {vote_percentage: .3f}% ({votes})\n"
        print(voter_output)

        #Save the candidate voter counts and perc to text file
        txt_file.write(voter_output)


    #Print the winner
    winning_candidate_summary = (
        f"_______________________\n"
        f"Winner:  {winning_candidate}\n"
        f"_______________________\n"
    )

    print (winning_candidate_summary)

    #save winner to text file
    txt_file.write(winning_candidate_summary)

