# code for DNA -> RNA transcription
# Accepts coding strand and template strand
# (str) -> (str)

def transcription(seq, coding_strand=True):
	seq = seq.upper()
	if coding_strand:
		rna = ['U' if nuc == 'T' else '' if nuc == ' ' or nuc == '\n' else nuc for nuc in seq]
		
	else:
		trans_map = {
		'A':'U', 'T':'A', 'G':'C', 'C':'G', '-':'-'
		}
		rna = [trans_map[nuc] if nuc in trans_map.keys() else '' if nuc == ' ' or nuc == '\n' 
		else nuc for nuc in seq]

	if not(set(rna).issubset({'A','U','G','C','-',''})):
		raise ValueError("String isn't fully DNA sequence")
	rna = "".join(rna)
	return(rna)

"""
#test case 1
DNA = 'ATGCATgtca\n agtctagc'
RNA = transcription(DNA)
EXP_OP = 'AUGCAUGUCAAGUCUAGC'
assert RNA == EXP_OP, "base case doesn't work"

#test case 2
DNA = 'ATGCATgtca\n agtctagc'
RNA = transcription(DNA, coding_strand=False)
EXP_OP = 'UACGUACAGUUCAGAUCG'
assert RNA == EXP_OP, "Template strand case doesn't work"

#test case 3 (error check)
DNA = 'ATgagtca shatcgagtcagtacg'
try:
	RNA = transcription(DNA)
except ValueError:
	print("Error check works")

print("All test cases cleared")
"""
