#This program asks the user to enter the projected amount of total sales, calculates the profit, and then displays the profit made from the amount.
#Date: 9/21/2018
#CTI-110 P2T1 - Sales Prediction
#Christian Davis
# Get the projected total sales
total_sales = float(input('Enter the projected sales: '))
# Calcuate the profit as 23 percent of total sales.
profit = total_sales * 0.23
# Display the profit.
print('The profit is $', format (profit, ',.2f'))
