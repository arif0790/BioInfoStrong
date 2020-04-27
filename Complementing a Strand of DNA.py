from Bio.Seq import Seq

DNA = Seq(input())
revcom = DNA.reverse_complement()

print(revcom)
