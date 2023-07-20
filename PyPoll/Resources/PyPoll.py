import csv

file_to_load = "election_data.csv"
file_to_output = "election_analysis.txt"

total_votes = 0

candidate_options = []
candidate_votes = {}

winning_candidate = ""
winnning_count = 0

with open(file_to_load) as election_data:
    reader=csv.DictReader(election_data)

    for row in reader:

        total_votes = total_votes + 1
        candidate_name = row["Candidate"]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
with open(file_to_output, "w") as txt_file:
    election_results = (
        f"Election Results\n"
        f"---------------\n"
        f"Total Votes: {total_votes}\n"
        f"--------------\n"
    )
    print(election_results)

    txt_file.write(f"{election_results}")

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes)*100

        if (votes > winnning_count):
            winnning_count = votes
            winning_candidate = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})"
        print(voter_output)
        txt_file.write(f"{voter_output}\n")

    winning_candidate_summary = (
        f"-----------------\n"
        f"Winner: {winning_candidate}\n"
        f"-----------------\n"
        )
    print(winning_candidate_summary)
    txt_file.write(f"{winning_candidate_summary}")