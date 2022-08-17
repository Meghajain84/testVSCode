#Open the data file.
#Write down the names of all the candidates.
#Add a vote count for each candidate.
#Get the total votes for each candidate.
#Get the total votes cast for the election.
#369711 data rows + header

# Import the datetime class from the datetime module.
#import datetime as dt
#Use the now() attribute on the datetime class to get the present time.
#now = dt.datetime.now()
# Print the present time.
#print("The time right now is ", now)

# importing csv and os 
import csv
import os

# Assign a variable for the file to load and the path.
#file_to_load = 'C:\Users\MEGHA\Documents\Rutgers\Python\Election_Analysis\Resources\election_results.csv' is giving some error
##file_to_load = os.path.join("Resources", "election_results.csv") OR file_to_load = 'Resources\election_results.csv' is giving same error but different from above
file_to_load = os.path.join("Resources", "election_results.csv") 
file_to_write = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
# election_data = open(file_to_load, 'r'), with this you need close() too

# Initialize a total vote counter.
total_votes = 0

# Candidate Options - List of unique candidates' names
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
#with open(r"C:\Users\MEGHA\Documents\Rutgers\Python\Election_Analysis\Resources\election_results.csv") as election_data:
with open(file_to_load, "r") as election_data:
    #print(election_data)

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
    #print(headers)

     # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_write, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: received {vote_percentage}% of the vote.")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    # print the summary on terminal
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)    
    

# Print the total votes.
#print(total_votes)

# Print the candidate list.
#print(candidate_options)

# Print the candidate vote dictionary.
#print(candidate_votes)

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = 'analysis\election_results.csv'
# Use the open statement to open the file as a text file.

    # Write some data to the file.
    #txt_file.write("Counties in the Election\n__________________________\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson\n")

