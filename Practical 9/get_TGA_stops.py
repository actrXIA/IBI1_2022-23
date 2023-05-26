import re
data = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
output = open("TGA_genes.fa", "w")
seq = ""
for line in data:
    if line.startswith(">"):    
        gene = re.split(" ", line, 1)[0]
        if re.search("TGA$", seq):
            output.write(seq)
        seq = ""
        count = 0
    elif not line.startswith(">"):
        count += 1
        if count == 1:
            seq += gene + "\n"
        seq += line
data.close()
output.close()
