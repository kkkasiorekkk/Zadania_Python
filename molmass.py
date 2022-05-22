# Napisz program molmass.py, który obliczy masę molową (kDa) sekwencji białkowej
# wprowadzonej przez użytkownika.

# Masa molowa sekwencji białkowej to suma mas wszystkich aminokwasów znajdujących się w sekwencji.
# Jeżeli sekwencja użytkownika zawiera znak, którego nie ma w słowniku protein_weights to przyjmij,
# że masa molowa tego znaku to 0.
# Na przykład, masa molowa sekwencji MKSX jest równa 149.2113 + 146.1876 + 105.0926 + 0 = 400.4915

protein_weights = {
   'A': 89.0932,
   'C': 121.1582,
   'D': 133.1027,
   'E': 147.1293,
   'F': 165.1891,
   'G': 75.0666,
   'H': 155.1546,
   'I': 131.1729,
   'K': 146.1876,
   'L': 131.1729,
   'M': 149.2113,
   'N': 132.1179,
   'O': 255.3134,
   'P': 115.1305,
   'Q': 146.1445,
   'R': 174.201,
   'S': 105.0926,
   'T': 119.1192,
   'U': 168.0532,
   'V': 117.1463,
   'W': 204.2252,
   'Y': 181.1885
}

protein_sequence = str(input('Enter protein sequence: '))
protein_sequence = protein_sequence.upper()
lst = list(protein_sequence)
molmass = 0

for i in range(len(lst)):
    if protein_weights.get(lst[i]) == None:
        molmass += 0
    else:
        molmass += protein_weights[lst[i]]

print(f'{molmass:.4f}')