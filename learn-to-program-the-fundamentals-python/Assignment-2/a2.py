def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    
    return get_length(dna1) > get_length(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    
    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    
    return dna1.rfind(dna2) > -1

def is_valid_sequence(dna_seq):
    
    nucleotides = 'ATCG'
    valid_nucleotide = True
    
    for char in dna_seq:
        if dna_seq in nucleotides:
            continue
        else:
            valid_nucleotide = False
            break
    
    return valid_nucleotide



        
def insert_sequence(dna, insert_seq, insert_index):
    
    dna_beginning = dna[:insert_index]
    dna_end = dna[insert_index:]
    new_dna_seq = dna_beginning + insert_seq + dna_end
    
    return new_dna_seq


def get_complement(nucleotide):
    
    if nucleotide == 'A':
        
        return 'T'
   
    elif nucleotide == 'T':
        
        return 'A'
    
    elif nucleotide == 'G':
        
        return 'C'
    
    elif nucleotide == 'C':
        
        return 'G'

def get_complementary_sequence(dna):
    
    comp_seq = ''
    
    for char in dna:
        comp_seq += get_complement(char)
    
    return comp_seq
