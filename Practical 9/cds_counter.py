import re
seq="ATGCAATCGACTACGATCTGAGAGGGCCTAA"
start_codon=re.split("ATG",seq,1)
counting=0
coding= re.findall(r"(TAA|TAG|TGA)",start_codon[1])
counting=len(coding)
print(counting)
