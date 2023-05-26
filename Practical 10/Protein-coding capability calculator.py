def calculator(seq):
    sequences = seq.upper() #change to capital letter
    start = sequences.find("ATG")
    stop = sequences.find("TGA")
    total = len(sequences)
    coding = stop - start
    coding_percentage = (coding/total) * 100
    if coding_percentage > 50:
        label = "protein-coding"
    elif coding_percentage < 10:
        label = "non-coding"
    else:
        label = "unclear"
    return coding_percentage ,label

dna = "aTGCTaaatGCatcgTGa"
result = calculator(dna)
print(result)
