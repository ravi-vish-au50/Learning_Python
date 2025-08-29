
# Arithmatices opratorer
a = int(input("Indtast et heltal: "))
b = int(input("Indtast et andet heltal: ")) 
print(a + b)  # Addition
print(a - b)  # Subtraktion
print(a * b)  # Multiplikation
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b) # Exponentiation
print(a // b) # Gulvdivision
print(-a)     # Negation
print(+b)     # Positiv tegn
print(a == b) # Lighed
print(a != b) # Ulighed
print(a > b)  # Større end
print(a < b)  # Mindre end 
print(a >= b) # Større end eller lig med
print(a <= b) # Mindre end eller lig med
print(a & b)  # Bitvis OG
print(a | b)  # Bitvis ELLER
print(a ^ b)  # Bitvis XOR
print(~a)     # Bitvis NOT 
print(a << 1) # Bitvis venstreforskydning
print(a >> 1) # Bitvis højreforskydning 
print(a and b) # Logisk OG
print(a or b)  # Logisk ELLER  
print(not a)   # Logisk IKKE
print(a if a > b else b) # Ternær operator
print(abs(-a)) # Absolut værdi
print(round(3.6)) # Afrunding
print(pow(a, b))  # Potens
remender = a % b
print(remender)   # Rest ved division
print(divmod(a, b)) # Kvotient og rest
print(sum([a, b])) # Sum af en liste

# comprehensions
squares = [x**2 for x in range(10)] # Liste comprehension
print(squares)
cubes = {x: x**3 for x in range(10)} # Dictionary comprehension
print(cubes)
unique_squares = {x**2 for x in range(-9, 10)} #
print(unique_squares) # Set comprehension
pairs = [(x, y) for x in range(3) for y in range(3)] # Nested comprehension
print(pairs) # Liste af tuples
print(len(squares)) # Længde af liste
print(min(squares)) # Minimum værdi i liste
print(max(squares)) # Maksimum værdi i liste
print(sorted(squares, reverse=True)) # Sorteret liste i faldende rækkefølge
print(list(reversed(squares))) # Omvendt liste  
print(squares.index(16)) # Indeks af værdi i liste
print(squares.count(16)) # Antal forekomster af værdi i liste
print(all(x > 0 for x in squares)) # Tjekker om alle elementer opfylder betingelse
print(any(x > 50 for x in squares)) # Tjekker om nogen elementer opfylder betingelse
print(list(map(lambda x: x + 1, squares))) # Anvender funktion på alle elementer i liste
print(list(filter(lambda x: x > 20, squares))) # Filtrerer elementer i liste baseret på betingelse
print(reduce(lambda x, y: x + y, squares)) # Reducerer liste til enkelt værdi ved at anvende funktion
from functools import reduce
from itertools import permutations, combinations

print(list(permutations([1, 2, 3], 2))) # Alle permutationer af længde 2
print(list(combinations([1, 2, 3], 2))) # Alle kombinationer af længde 2   
print(list(combinations(range(4), 3))) # Alle kombinationer af længde 3 fra range
print(list(permutations('abc', 2))) # Alle permutationer af længde 2 fra string

# logical operators
x = True   
y = False
print(x and y)  # Logisk OG
print(x or y)   # Logisk ELLER
print(not x)    # Logisk IKKE
print(x if x else y) # Ternær operator

# Bitwise operators 
a = 5  # Binært: 0101
b = 3  # Binært: 0011   
print(a & b)  # Bitvis OG: 0001 (1)
print(a | b)  # Bitvis ELLER: 0111 (7)  
print(a ^ b)  # Bitvis XOR: 0110 (6)
print(~a)     # Bitvis NOT: 1010 (-6)   
print(a << 1) # Bitvis venstreforskydning: 1010 (10)
print(a >> 1) # Bitvis højreforskydning: 0010 (