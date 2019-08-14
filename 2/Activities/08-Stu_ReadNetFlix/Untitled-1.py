import os
import csv

title = []
rating = []
score = []

path_of_file = os.path.join('Resources', 'netflix_ratings.csv')
with open(path_of_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print("CSV Header: " + str(csv_header))

    for row in csvreader:
        print(row[0],row[1],row[5])
        title.append(row[0])
        rating.append(row[1])
        score.append(row[5])


ans = 'y'
found = False
while ans == 'y':
  input_value = input("what would you like to see?: ")
  for i in range(len(title)):
      if title[i] == input_value:
          found = True
          print("found! here's the rating and score: " + rating[i] + ',' + score[i])

if found != True:
    print('sorry nothing there...')
