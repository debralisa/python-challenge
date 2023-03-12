#python challenge PyPoll script

#Dependencies
import os
import csv

#from pathlib import Path
#election_data_csv = Path("python-challenge", "PyPoll", "election_data.csv") 

#File locations for read and write files
#election_data_csv = "/Users/debralisa3/Dropbox/python-challenge/PyPoll/Resources/election_data.csv"
#election_out_txt = "/Users/debralisa3/Dropbox/python-challenge/PyPoll/Analysis/election_data_out.txt"

#path locations for input and output files. First couple unsuccessful attempts are above and commented out to show progression. 

election_data_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'election_data.csv')
election_out_txt = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'analysis', 'election_data_out.txt')

#Set total vote counter
vote_total = 0

#Setup candidate options and vote counters
candidate_options = []
candidate_votes = {}

#Setup winning candidate variable and winning counter
winning_candidate = ""
winning_count = 0

#Read in the csv input file and convert into list of dictionaries
with open(election_data_csv, "r") as election_data:
    reader = csv.DictReader(election_data)

    #For statement to run through each row
    for row in reader:

        #add/increment vote count to the total vote count and get candidate name per row
        vote_total = vote_total + 1
        candidate_name = row["Candidate"]

        #if condition for no candidate name match
        if candidate_name not in candidate_options:

            #append name to the candidate names list and start specific candidate vote counter
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
    
        #then add/increment vote count to specific candidate vote counter
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#Print results to screen and write data to output text file
with open(election_out_txt, "w") as txt_file:

     election_results = (
        f"\nElection Results\n"
        f"______________________\n"
        f"Total Votes:  {vote_total}\n"
        f"______________________\n"
    )
    print(election_results)

    txt_file.write(election_results)

    #Next module is to calculate the candidates' percentages and vote counts with a for loop for each candidate
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes)/float(vote_total) * 100

        #Determine winner and vote count
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        #Print each candidate, percentage (to the 3rd decimal) and actual voter count
        voter_output = f"{candidate}: {vote_percentage: .3f}% ({votes})\n"
        print(voter_output)

        #Save the candidate voter summary information from the print calculations to the output text file
        txt_file.write(voter_output)


    #Print the winner
    winning_candidate_summary = (
        f"_______________________\n"
        f"Winner:  {winning_candidate}\n"
        f"_______________________\n"
    )

    print (winning_candidate_summary)

    #save winner information to the output text file
    txt_file.write(winning_candidate_summary)

