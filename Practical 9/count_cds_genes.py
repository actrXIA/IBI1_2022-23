import re
data = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
print("Please enter a stop codon")
stop_codons = input("")
if re.match("TAA|TAG|TGA", stop_codons):
    output = open(stop_codons+"_stop_genes.fa", "w")
    seq = ""
    for line in data:
        if line.startswith(">"):
            seq += "\n"
            gene = re.split(" ", line, 1)[0]
            if re.findall(stop_codons, seq):
                num = len(re.findall(stop_codons, seq))
                output.write(seq%(str(num)))
            seq=""
            counter=0
            num=0
        elif not line.startswith(">"):
            counter+=1
            if counter==1:
                seq+=gene+"coding_sequences:%s"+"\n"
                seq+=line[:-1]
else:
     print("The input is not a stop codon")
data.close()
output.close()
