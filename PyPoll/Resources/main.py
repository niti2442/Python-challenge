#Modules
import os
import csv
csvpath= os.path.join(".", "Documents", "Python-challenge", "PyPoll", "Resources", "election_data.csv")
#Open csv file
with open (csvpath, encoding='utf') as csvfile:
csvreader = csv.reader(csvfile, delimiter=",")
#Total number of votes cast
next(csvreader)
data= list(csvreader)
row_count= len(data)
#New list from CSV column
candilist= list()
tally=list()
for i in range (0,row_count):
candidate= data[i][2]
tally.append(candidate)
if candidate not in candilist:
candilist.append(candidate)
candicount= len(candilist)
#Total number of votes won and percentage won
votes= list()
percentage= list()
for j in range (0,candicount):
name= candilist[j]
votes.append(tally.count(name))
vprct= votes[j]/row_count
percentage.append(vprct)
#Winner 
winner= votes.index(max(votes))
#Print Analysis
print("Election Results")
print("----------------------\n")
print("Total Votes: %d"%total)
print("--------------------\n")
percentage= (data[i]/total)*100
percent_list.append(percentage)
print("%s:%f(%d)"%(i, percentage, data[i]))
print("--------------------\n")
print("Winner:", candidates[percent_list.index(max(percent_list))])
print("\t--------------------\n")
