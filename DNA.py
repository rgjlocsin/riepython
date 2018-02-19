countC=0.0
countG=0.0

DNA = open("DNA.txt").read();
totalLength = len(DNA)


for i in range(len(DNA)):
    if DNA[i] == "C":
        countC = countC+1.0

    if DNA[i] == "G":
        countG = countG+1.0

Total = countC+countG

print("Number of C: ", countC)
print("Number of G: ", countG)
print("Total number of C+G: ", Total)
print("Total number of DNA: ", len(DNA))
print("Percentage: ", ((Total/len(DNA))*100.0))
