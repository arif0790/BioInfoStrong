from Bio.Seq import Seq

DNA = Seq(input())
revcom = str(DNA.reverse_complement())

print(revcom)
