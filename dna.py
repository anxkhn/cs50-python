from sys import argv
from sys import exit
import csv

if len(argv) != 3:
    print("Usage: dna.py csv txt")
    exit(1)

# open the DNA sequence and read its contents into memory.
txtfile = open(argv[2], "r")
if not txtfile:
    print("Could not open file.")
    exit(1)
dna = txtfile.read()

# If the STR counts match exactly with any of the individuals in the CSV file, print out the name of the matching individual.
with open(argv[1]) as csvfile:
    reader = csv.DictReader(csvfile)

    # For each of the STRs, compute the longest run of consecutive repeats of the STR in the DNA sequence to identify
    keys = reader.fieldnames.copy()
    del keys[0]
    keysMax = []
    for j in range(len(keys)):
        keysMax.append(0)
        for i in range(len(dna)):
            count = 0
            if dna[i:i+len(keys[j])]  == keys[j]:
                while dna[i:i+len(keys[j])]  == keys[j]:
                    i += len(keys[j])
                    count += 1
                if count > keysMax[j]:
                    keysMax[j] = count


#Compare each row of CSV with STR results
found = False
with open(argv[1]) as csvfile:
    reader = csv.reader(csvfile)
    next(reader) #Skip header CSV
    for row in reader:
        corresp = 0
        for i in range(len(keysMax)):
            if int(row[i+1]) == keysMax[i]:
                corresp += 1
        if corresp == len(keysMax):
            match = row[0]
            found = True
            break
        #if int(row[1]) == keysMax[0] and int(row[2]) == keysMax[1] and int(row[3]) == keysMax[2]:
            #match = row[0]
            #found = True

# Print match
if found == True:
    print(match)
else:
    print("No match.")