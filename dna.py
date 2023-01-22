import random
import math

nucleotides = ['A', 'C', 'G', 'T']
dna_length = 100000000  # 100 million nucleotides

dna_sample = ''.join(random.choices(nucleotides, k=dna_length))

# 1 byte = 8 bits
# 1 nucleotide = 2 bits (since there are 4 possible nucleotides)
# 1 megabyte = 10^6 bytes
# 1 gigabyte = 10^9 bytes

dna_sample_size_bits = dna_length * 2
dna_sample_size_bytes = dna_sample_size_bits / 8
dna_sample_size_mb = dna_sample_size_bytes / (10 ** 6)
dna_sample_size_gb = dna_sample_size_bytes / (10 ** 9)

print("DNA Sample Size: {:.2f} megabytes / {:.2f} gigabytes".format(dna_sample_size_mb, dna_sample_size_gb))
