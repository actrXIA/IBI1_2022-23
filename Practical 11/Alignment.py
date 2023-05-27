cat=open("ACE2_cat.fa")
mouse=open("ACE2_mouse.fa")
human=open("ACE2_human.fa")

cat_seq=cat.readlines()
mouse_seq=mouse.readlines()
human_seq=human.readlines()
#read seq

BLOSUM=open("BLOSUM62.txt")
BLOSUM_matrix = BLOSUM.readlines()
BLOSUM_matrix = [line.rstrip() for line in BLOSUM_matrix]

dictionary={}
#prepare dictionary


for i in range(1,len(BLOSUM_matrix)):
     BLOSUM_matrix[i]=BLOSUM_matrix[i].split()[1:]
keys=BLOSUM_matrix[0].replace(" ","")
values=BLOSUM_matrix[1:]

for i in range(0,len(keys)):
    for j in range(0,len(keys)):
        dictionary[(keys[i],keys[j])]=int(values[i][j])

def align(seq1,seq2):
    seq_match={}
    seq1_name=seq1[0]
    seq2_name=seq2[0]
    seq1_list=seq1[1].rstrip()
    seq2_list=seq2[1].rstrip()
    score=0
    same=0
    compair = list(zip(seq1_list, seq2_list))
    for pair in compair:
        if pair[0]==pair[1]:
            same += 1
        score += dictionary[pair]
    per = same/len(seq1)*100

    print("Seq:",seq1_name,seq2_name)
    print("Alignment Matrix: BLOSUM62")
    print("Alignment Score:", score)
    print("Identical Percentage:", per)
    return

cat.close()
mouse.close()
human.close()
