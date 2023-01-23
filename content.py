import random

def generate_dna(length,gc_content):
    gc_count = int(gc_content * length / 100)
    at_count = length - gc_count
    gc_bases = ['G','C']
    at_bases = ['A','T']
    return ''.join(random.choice(gc_bases) for _ in range(gc_count))+''.join(random.choice(at_bases) for _ in range(at_count))

print(generate_dna(10,50))
