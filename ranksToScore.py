import csv

f = open("gp-100_scores.txt")

scores = []
for line in f:
    line = line.split()
    scores.append(line)

f.close()

records = []

with open("RanksToScore.csv") as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ',')
    for row in csvReader:
        record = {}
        record['Roll No'] = row[1]
        if int(row[0]) > 100:
            record['Score'] = 0
        else:
            record['Score'] = int(scores[int(row[0])][1])
        records.append(record)

filename = 'scores.csv'
with open(filename, 'w') as f: 
    w = csv.DictWriter(f,['Roll No', 'Score']) 
    w.writeheader() 
    for record in records: 
        w.writerow(record) 
