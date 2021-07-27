# Central Dogma code
# Sarvesh Menon

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
if RNA == EXP_OP:
	print('Test works')

#test case 2
DNA = 'ATGCATgtca\n agtctagc'
RNA = transcription(DNA, coding_strand=False)
EXP_OP = 'UACGUACAGUUCAGAUCG'
if RNA == EXP_OP:
	print('Test works')

#test case 3 (error check)
DNA = 'ATgagtca shatcgagtcagtacg'
try:
	RNA = transcription(DNA)
except ValueError:
	print("Error check works")
"""
