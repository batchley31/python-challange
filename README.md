# python-challange

For both the PyPoll and PyBank I started my code with importing the CSV and then labling my CSV's with "file_to_load" and the data I am outputing to "file_to_ouptut" in a test file.

Next I labeled all the variables I was going to use nad set the starting points whether it was 0 for numbered variables or sqaure brackets to detemrine the list.

# PyBank Calulations 
In my PyBank.py file I opened my CSV to look at the date as "revenue_data" and used that to add up the total amount of months in the data set. I then set the code to calculate the total revenue by looking in the second part of the list or "1" since the first is techinically "0".  Then I calclulated all the revenue together by having it add it up month by month.

With calculating the greatest increase and greatest decrease in profits I looked for each amount and how much it was compared to the month before.  I added to the list for revenue change and then said that if the change in reveneue is greater than the previous month replace that wiht what was there before and look to the next.  Once it couldn't find a month with a greater chnage in revenue I had it output what month and year that was, and also had it put the greatest increase in paranthesis next to it.  For the greatest decrease I did the exact same thing but had it look for the decrease being bigger than the previous change and output it the same way.

To calculate the average revenue I took the total of all the changes in revenue for each month and divided it by how many times it changed, or for how many months we are tracking the revenue change.

For my output at the end I name all the things I wanted to calculate and then but in curly brakets if they were to equal anything. I used a backslash "n" to tell the code when I wanted to start the next line of my labels. At the end I had it output everything as a test file.

#PyPoll Calculations
For the beginning of the polling I had the code look for all the votes in the whole file and add them up.  While it was adding up the votes I had it keep track of all the different names that were voted on.  So as it ran through all the duplicates it would only add a cnadidates name once it found a name it hasnt seen before while counting.  

For the first output I created a dictionary of everythign I wanted to see in the first set of data for total votes and printed that as it own function.
For the second function I made the votes equal how many votes one candidate had in total and then later used to that present the winning count of votes for a certian candidate. I calculated that by taking the total votes for each candidte and saying that the greatest number of votes for a certian candidate would equal the winning count of votes for that particual candidate.  I labeled the "winning Candidate" by having that equal the candidate with the highest votes that were determined by votes.

I calculated the percentage of votes by taking the votes for each candidate and dividing by total amount of votes for all candidates.

My output at the bottom looked for the name of the candidate with the highest votes from the previous output and labeled the winner underneath. I used \"n" for line breakes just like I did for PyBank to make it look nice and clean and easy to read. 
