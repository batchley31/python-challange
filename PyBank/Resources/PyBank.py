import csv 

file_to_load = "budget_data.csv"
file_to_output = "PyBank.txt"

total_months = 0
previous_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greastest_decrease = ["", 9999999999999]
total_revenue = 0

with open(file_to_load) as revenue_data:
    reader = csv.reader(revenue_data)
    header = next(reader)
    first_row = next(reader)
    total_months = 1
    total_revenue = int(first_row[1])
    previous_revenue = total_revenue

    for row in reader:

        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])

        revenue_change = int(row[1]) - previous_revenue
        previous_revenue = int(row[1])
        revenue_change_list.append(revenue_change)
        

        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = revenue_change
        if (revenue_change < greastest_decrease[1]):
            greastest_decrease[0] = row[0]
            greastest_decrease[1] = revenue_change

revenue_average = sum(revenue_change_list) / len(revenue_change_list)

output = (
    f"Fianacial Analysis\n"
    f"-------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Change: ${revenue_average}\n"
    f"Greastest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greastest Decrease in Profits: {greastest_decrease[0]} (${greastest_decrease[1]})" 
)

print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)