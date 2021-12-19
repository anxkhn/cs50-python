# Checked with python docs for functions and libs
from sys import argv
from sys import exit
import csv

if len(argv) != 3:
    print("Usage: dna.py csv txt")
    exit(1)

# DNA sequence into memory.
txtfile = open(argv[2], "r")
if not txtfile:
    print("Can't not open file.")
    exit(1)
dna = txtfile.read()

# STR count matching algo.
with open(argv[1]) as csvfile:
    reader = csv.DictReader(csvfile)
    keys = reader.fieldnames.copy()
    del keys[0]
    keysMax = []
# loops with cases
    for j in range(len(keys)):
        keysMax.append(0)
        for i in range(len(dna)):
            count = 0
            if dna[i:i+len(keys[j])] == keys[j]:
                while dna[i:i+len(keys[j])] == keys[j]:
                    i += len(keys[j])
                    count += 1
                if count > keysMax[j]:
                    keysMax[j] = count

# Compareing values while skipping header files
found = False
with open(argv[1]) as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        corresp = 0
        for i in range(len(keysMax)):
            if int(row[i+1]) == keysMax[i]:
                corresp += 1
        if corresp == len(keysMax):
            match = row[0]
            found = True
            break
# Printing output
if found == True:
    print(match)
else:
    print("No match.")