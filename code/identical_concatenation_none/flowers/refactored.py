# --- Flower Parts ---

# Petals
def rose_petals():
    print(" @@@@")
    print("@@()@@")
    print(" @@@@")

def carnation_petals():
    print(" vVVVv")
    print(" (___)")

# Stems
def short_stem():
    print("   Y")
    print("  \\|/")

def long_stem():
    print("   Y")
    print("  \\|/")
    print(" \\ | /")

# Base (same for all)
def base():
    print("(((|)))")

# --- Full Flowers (assembled from parts) ---

def long_stem_rose():
    print("Long-stem Rose")
    rose_petals()
    long_stem()
    base()
    print()

def short_stem_rose():
    print("Short-stem Rose")
    rose_petals()
    short_stem()
    base()
    print()

def short_stem_carnation():
    print("Short-stem Carnation")
    carnation_petals()
    short_stem()
    base()
    print()

def long_stem_carnation():
    print("Long-stem Carnation")
    carnation_petals()
    long_stem()
    base()
    print()

# --- Print all flowers ---

long_stem_rose()
short_stem_rose()
short_stem_carnation()
long_stem_carnation()
