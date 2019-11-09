{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 514,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Modules\n",
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 515,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Set file path\n",
    "budget_csv = os.path.join(\"..\",\"PyBank\",\"Resources\",\"budget_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 516,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Set variables\n",
    "total_months= 0\n",
    "total_profitloss= 0\n",
    "monthly_change= 0\n",
    "start= 0\n",
    "dates= []\n",
    "profits= []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 517,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Open and read CSV file with delimiter set\n",
    "with open(budget_csv, newline=\"\", encoding=\"utf-8\") as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=\",\")\n",
    "    csv_header = next(csvreader)    \n",
    "    row = next(csvreader)\n",
    "    total_months = 1\n",
    "    total_profitloss += int(row[1])\n",
    "    start = int(row[1])\n",
    "    \n",
    "    for row in csvreader:\n",
    "        dates.append(row[0])\n",
    "        change = int(row[1]) - start\n",
    "        profits.append(change)\n",
    "        start = int(row[1])\n",
    "        total_months +=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 518,
   "metadata": {},
   "outputs": [],
   "source": [
    "total_profitloss = total_profitloss + int(row[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 519,
   "metadata": {},
   "outputs": [],
   "source": [
    "greatest_increase = max(profits)\n",
    "highest_index = profits.index(greatest_increase)\n",
    "greatest_date = dates[highest_index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 520,
   "metadata": {},
   "outputs": [],
   "source": [
    "greatest_decrease = min(profits)\n",
    "lowest_index = profits.index(greatest_decrease)\n",
    "worst_date = dates[lowest_index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 521,
   "metadata": {},
   "outputs": [],
   "source": [
    "average_change = sum(profits)/len(profits)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 522,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "---------------------------\n",
      "Total Months: 86\n",
      "Total: $ 1538983\n",
      "Average Change: $-2315.12\n",
      "Greatest Increase in Profits:, Feb-12,($1926159)\n",
      "Greatest Decrease in Profits:, Sep-13,($-2196167)\n"
     ]
    }
   ],
   "source": [
    "print(f\"Financial Analysis\")\n",
    "print(f\"---------------------------\")\n",
    "print(f\"Total Months: {total_months}\")\n",
    "print(f\"Total: $ {(total_profitloss)}\")\n",
    "print(f\"Average Change: ${average_change:.2f}\")\n",
    "print(f\"Greatest Increase in Profits:, {greatest_date},(${str(greatest_increase)})\")\n",
    "print(f\"Greatest Decrease in Profits:, {worst_date},(${str(greatest_decrease)})\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 523,
   "metadata": {},
   "outputs": [],
   "source": [
    "output_file= os.path.join('..',\"PyBank\",\"Resources\",\"budget_data_completed.text\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 524,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(output_file,'w',)as txtfile:\n",
    "    txtfile.write(f\"Financial Analysis\")\n",
    "    txtfile.write(f\"---------------------------\")\n",
    "    txtfile.write(f\"Total Months: {total_months}\")\n",
    "    txtfile.write(f\"Total: ${total_profitloss}\")\n",
    "    txtfile.write(f\"Average Change: ${average_change:.2f}\")\n",
    "    txtfile.write(f\"Greatest Increase in Profits:, {greatest_date},(${str(greatest_increase)})\")\n",
    "    txtfile.write(f\"Greatest Decrease in Profits:, {worst_date},(${str(greatest_decrease)})\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:PythonData] *",
   "language": "python",
   "name": "conda-env-PythonData-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
