{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 210,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import dependencies\n",
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 211,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Set path for CSV\n",
    "election_csv = os.path.join(\"election_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set Variables\n",
    "total_votes = 0\n",
    "Khan_votes = 0\n",
    "Correy_votes = 0\n",
    "Li_votes = 0\n",
    "Otooley_votes = 0\n",
    "winner = [\"Khan\",\"Correy\", \"Li\", \"OTooley\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 213,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Open/Read CSV File\n",
    "with open(election_csv, newline= '') as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter= ',')\n",
    "    csv_header = next(csvfile)\n",
    "    \n",
    "    for row in csvreader:\n",
    "        total_votes = total_votes + 1\n",
    "        \n",
    "        if (row[2] == \"Khan\"):\n",
    "            Khan_votes += 1\n",
    "        elif (row[2] == \"Correy\"):\n",
    "            Correy_votes +=1\n",
    "        elif (row[2] == \"Li\"):\n",
    "            Li_votes +=1\n",
    "        else:\n",
    "            Otooley_votes +=1\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 214,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate percentage of win votes for each person\n",
    "Khan_percent = Khan_votes / total_votes\n",
    "Correy_percent = Correy_votes / total_votes\n",
    "Li_percent = Li_votes / total_votes\n",
    "Otooley_percent = Otooley_votes / total_votes "
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "winner = max(Khan_votes, Correy_votes, Li_votes, Otooley_votes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 215,
   "metadata": {},
   "outputs": [],
   "source": [
    "if winner == Khan_votes:\n",
    "    winner_name = \"Khan\"\n",
    "elif winner == Correy_votes:\n",
    "    winner_name = \"Correy\"\n",
    "elif winner == Li_votes:\n",
    "    winner_name == \"Li\"\n",
    "else:\n",
    "    winner_name == \"O'Tooley\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 216,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "-----------------------------\n",
      " Total Votes: 1048575\n",
      " Khan: 63.094%(661583)\n",
      " Li: 13.958%(146360)\n",
      " Correy 19.936%(209046)\n",
      " Otooley 3.012%(0.03012278568533486)\n",
      "-----------------------------\n",
      "Winner: []\n"
     ]
    }
   ],
   "source": [
    "# Analysis\n",
    "print(f\"Election Results\")\n",
    "print (f\"-----------------------------\")     \n",
    "print (f\" Total Votes: {total_votes}\")\n",
    "print (f\" Khan: {Khan_percent:.3%}({Khan_votes})\")\n",
    "print (f\" Li: {Li_percent:.3%}({Li_votes})\")\n",
    "print (f\" Correy {Correy_percent:.3%}({Correy_votes})\")\n",
    "print (f\" Otooley {Otooley_percent:.3%}({Otooley_percent})\")       \n",
    "print (f\"-----------------------------\")\n",
    "print (f\"Winner: []\")\n",
    "       "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
   "metadata": {},
   "outputs": [],
   "source": [
    "# set file to write text file to\n",
    "output_file= os.path.join(\"election_data_completed.text\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 218,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Winner: []\n"
     ]
    }
   ],
   "source": [
    "#write text data\n",
    "with open(output_file,'w',)as txtfile:\n",
    "    txtfile.write(f\"Election Results\")\n",
    "    txtfile.write(f\"---------------------------\")\n",
    "    txtfile.write(f\"Total Votes: {total_votes}\")\n",
    "    txtfile.write(f\"---------------------------\")\n",
    "    txtfile.write(f\" Khan: {Khan_percent:.3%}({Khan_votes})\")\n",
    "    txtfile.write(f\" Li: {Li_percent:.3%}({Li_votes})\")\n",
    "    txtfile.write(f\" Correy {Correy_percent:.3%}({Correy_votes})\")\n",
    "    txtfile.write(f\" Otooley {Otooley_percent:.3%}({Otooley_percent})\")\n",
    "    txtfile.write(f\"-----------------------------\")\n",
    "    print (f\"Winner: []\")"
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
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
