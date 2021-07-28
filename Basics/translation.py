# Translation mRNA -> protein code
# Accepts frame (-ve frames for reverse complement strand) 
# and custom codon tables 
# (str) -> (str)

std_codon_table = {
	'UUU':'F','UUC':'F',
	'UUA':'L','UUG':'L','CUU':'L','CUC':'L','CUA':'L','CUG':'L',
	'AUU':'I','AUC':'I','AUA':'I',
	'AUG':'M',
	'GUU':'V','GUC':'V','GUA':'V','GUG':'V',
	'UCU':'S','UCC':'S','UCA':'S','UCG':'S',
	'CCU':'P','CCC':'P','CCA':'P','CCG':'P',
	'ACU':'T','ACC':'T','ACA':'T','ACG':'T',
	'GCU':'A','GCC':'A','GCA':'A','GCG':'A',
	'UAU':'Y','UAC':'Y',
	'UAA':'*','UAG':'*','UGA':'*',
	'CAU':'H','CAC':'H',
	'CAA':'Q','CAG':'Q',
	'AAU':'N','AAC':'N',
	'AAA':'K','AAG':'K',
	'GAU':'D','GAC':'D',
	'GAA':'E','GAG':'E',
	'UGU':'C','UGC':'C',
	'UGG':'W',
	'CGU':'R','CGC':'R','CGA':'R','CGG':'R','AGA':'R','AGG':'R',
	'AGU':'S','AGC':'S',
	'GGU':'G','GGC':'G','GGA':'G','GGG':'G',
	}

def translation(seq, frame=1, codon_table=std_codon_table):
	if frame not in range(-3,4):
		raise ValueError("Frame Invalid")

	seq = seq.upper().replace(' ','').replace('\n','')
	if frame<0:
		seq = ['A' if nuc == 'U' else 'U' if nuc == 'A' 
		else 'G' if nuc == 'C' else 'C' if nuc == 'G' else nuc for nuc in seq]
		seq = "".join(seq)[frame::-1]
	else:
		seq = seq[frame-1 if frame>0 else frame:]

	protein = [codon_table[seq[i:i+3]] if seq[i:i+3] in codon_table.keys() else '' if len(seq[i:i+3])<3 
	else 'X' if '-' in seq[i:i+3] else 'Err' for i in range(0,len(seq),3)]

	if 'Err' in protein:
		raise ValueError("Sequence isn't mRNA")
	else:
		protein = "".join(protein)

	return(protein)

"""
#test case 1
RNA = 'uacguaca \nguucAGAucguga'
EXP_OP = 'YVQFRS*'
protein = translation(RNA)
assert protein == EXP_OP, "Base case doesn't work"

#test case 2
RNA = 'aucgccuagcggggaaacgauaccaccc'
EXP_OP = 'GGIVSPLGD'
protein = translation(RNA,frame=-2)
assert protein == EXP_OP, "Reverse frames don't work"

#test case 3 (error check)
RNA = 'atagcatgcatgactgac'
try:
	protein = translation(RNA)
except ValueError:
	print("Error check works")

print("All test cases cleared")
"""
