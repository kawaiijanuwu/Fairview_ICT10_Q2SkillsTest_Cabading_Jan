from pyscript import document
# Jan Cabading | 10 Sapphire

#List of non-metals stored in a tuple
nonmetals = {
    "H": ("Hydrogen", 1, 1.008),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Se": ("Selenium", 34, 78.971),
    "F": ("Fluorine", 9, 18.998),
    "Cl": ("Chlorine", 17, 35.45),
    "Br": ("Bromine", 35, 79.904),
    "I": ("Iodine", 53, 126.90),
    "At": ("Astatine", 85, 210),
    "Ts": ("Tennessine", 117, 294),
    "He": ("Helium", 2, 4.0026),
    "Ne": ("Neon", 10, 20.180),
    "Ar": ("Argon", 18, 39.95),
    "Kr": ("Krypton", 36, 83.798),
    "Xe": ("Xenon", 54, 131.29),
    "Rn": ("Radon", 86, 222),
    "Og": ("Oganesson", 118, 294)
}

def search_element(event=None):
    # get user input string from input
    symbol_input = document.getElementById("symbolInput").value.strip()
    
    # use .get, in "element is not found", added "-" since its a tuple because info in line 39 needs 3 variables
    info = nonmetals.get(
        symbol_input, 
        ("Element is not found!" "-" "-")
    )
    
    # extract details from tuple, to get info 
    name, atomic_num, atomic_mass = info
    
   # Display details to specific target ids
    display(symbol_input, target="displaySymbol")
    display(name, target="displayName")
    display(atomic_num, target="displayNumber")
    display(atomic_mass, target="displayMass")



  