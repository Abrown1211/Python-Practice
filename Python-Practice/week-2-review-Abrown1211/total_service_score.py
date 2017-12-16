# Please do your work for problem two in this file

DaysOfScores = eval(input("How many days of scores?: "))

TotalScore = 0

for i in range(DaysOfScores):
    print("Enter the score for the day", i+1 ,":", end="")
    DailyScore = int(input())
    TotalScore = DailyScore + TotalScore
print("The total score of the", DaysOfScores, "days is", TotalScore)

