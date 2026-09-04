# Case Study 1 - Branching Statements

# Player 1
runs1 = 148
balls1 = 50
wickets1 = 4
conceded1 = 29
overs1 = 2
catches1 = 3

sr1 = (runs1 / balls1) * 100
eco1 = conceded1 / overs1

if runs1 >= 50 and sr1 >= 120:
    bat1 = "Excellent Batter"
elif runs1 >= 30 and sr1 >= 100:
    bat1 = "Good Batter"
elif runs1 >= 20:
    bat1 = "Average Batter"
else:
    bat1 = "Poor Batter"

if wickets1 >= 3 and eco1 <= 6:
    bowl1 = "Excellent Bowler"
elif wickets1 >= 2 and eco1 <= 8:
    bowl1 = "Good Bowler"
elif wickets1 >= 1:
    bowl1 = "Average Bowler"
else:
    bowl1 = "Poor Bowler"

if catches1 >= 2:
    field1 = "Outstanding Fielder"
elif catches1 == 1:
    field1 = "Active Fielder"
else:
    field1 = "Needs Improvement"

if bat1 == "Excellent Batter" and bowl1 == "Excellent Bowler":
    overall1 = "Star All-Rounder"
elif bat1 == "Good Batter" and bowl1 == "Good Bowler":
    overall1 = "Strong All-Rounder"
elif bat1 == "Good Batter" or bowl1 == "Good Bowler":
    overall1 = "Supporting All-Rounder"
else:
    overall1 = "Needs Improvement"

print("Player 1")
print("Strike Rate:", sr1)
print("Economy Rate:", eco1)
print("Batting:", bat1)
print("Bowling:", bowl1)
print("Fielding:", field1)
print("Overall:", overall1)


# Player 2
runs2 = 179
balls2 = 62
wickets2 = 8
conceded2 = 32
overs2 = 3
catches2 = 2

sr2 = (runs2 / balls2) * 100
eco2 = conceded2 / overs2

if runs2 >= 50 and sr2 >= 120:
    bat2 = "Excellent Batter"
elif runs2 >= 30 and sr2 >= 100:
    bat2 = "Good Batter"
elif runs2 >= 20:
    bat2 = "Average Batter"
else:
    bat2 = "Poor Batter"

if wickets2 >= 3 and eco2 <= 6:
    bowl2 = "Excellent Bowler"
elif wickets2 >= 2 and eco2 <= 8:
    bowl2 = "Good Bowler"
elif wickets2 >= 1:
    bowl2 = "Average Bowler"
else:
    bowl2 = "Poor Bowler"

if catches2 >= 2:
    field2 = "Outstanding Fielder"
elif catches2 == 1:
    field2 = "Active Fielder"
else:
    field2 = "Needs Improvement"

if bat2 == "Excellent Batter" and bowl2 == "Excellent Bowler":
    overall2 = "Star All-Rounder"
elif bat2 == "Good Batter" and bowl2 == "Good Bowler":
    overall2 = "Strong All-Rounder"
elif bat2 == "Good Batter" or bowl2 == "Good Bowler":
    overall2 = "Supporting All-Rounder"
else:
    overall2 = "Needs Improvement"

print("Player 2")
print("Strike Rate:", sr2)
print("Economy Rate:", eco2)
print("Batting:", bat2)
print("Bowling:", bowl2)
print("Fielding:", field2)
print("Overall:", overall2)