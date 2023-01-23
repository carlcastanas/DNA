import random

def generate_dna(length):
    bases = ['A', 'C', 'G', 'T']
    return ''.join(random.choice(bases) for _ in range(length))

print(generate_dna(10))
