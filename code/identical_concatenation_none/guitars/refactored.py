def print_head() -> None:
    print("        ___")
    print("      o|* *|o")
    print("      o|* *|o")
    print("      o|* *|o")
    print("       \===/")

def print_retro_head() -> None:
    print("       ._-_.")
    print("      +|\G/|+")
    print("      +|\./|+")
    print("      +|\./|+")
    print("       \===/")

def print_neck() -> None:
    print("        |||")
    print("        |||")

def print_body() -> None:
    print("     ___|||___")
    print("    /   |||   \ ")
    print("   /    |||    \ ")
    print("  |     |||     |")
    print("   \   (|||)   /")
    print("    |   |||   |")
    print("   /    |||    \ ")
    print("  /     |||     \ ")
    print(" /      |||      \ ")
    print(" |     [===]     |")
    print("  \             /")
    print("   '._________.'")

def print_classic_guitar() -> None:
  print_head()
  print_neck()
  print_body()

def print_retro_guitar() -> None:
  print_retro_head()
  print_neck()
  print_body()

def print_long_guitar() -> None:
  print_head()
  print_neck()
  print_neck()
  print_body()

def main() -> None:
  print("Classic guitar")
  print_classic_guitar()
  print("Retro guitar")
  print_retro_guitar()
  print("Long guitar")
  print_long_guitar()

main()