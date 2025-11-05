# ASCII Fish 

def print_tail(size = 1):
    print(3*" " + 3*"v")
    print(4*" " + "v")

def print_body(size = 1):
    print(3*" " + "v" + "o" + "v")
    print(2*" " + "v" + 3*"o" + "v")
    print(1*" " + "v" + 5*"o" + "v")
    print(0*" " + "v" + 7*"o" + "v")

def print_head(size = 1):
    print(1*" " + "v" + 2*"o" + 1*" " + 2*"o" + "v")
    print(2*" " + "v" + 0*"o" + 3*" " + 0*"o" + "v")

print_tail()
print_body()
print_head()

# Bigger ASCII Fish

def print_tail_big(size = 2):
    print(4* " " + 5*"v")
    print(5* " " + 3*"v")
    print(6* " " + "v")

def print_body_big(size = 2):
    print(5*" " + "v" + "o" + "v")
    print(4*" " + "v" + 3*"o" + "v")
    print(3*" " + "v" + 5*"o" + "v")
    print(2*" " + "v" + 7*"o" + "v")
    print(1*" " + "v" + 9*"o" + "v")
    print(0*" " + "v" + 11*"o" + "v")

def print_head_big(size = 2):
    print(1*" " + "v" + 4*"o" + 1*" " + 4*"o" + "v")
    print(2*" " + "v" + 2*"o" + 3*" " + 2*"o" + "v")
    print(3*" " + "v" + 0*"o" + 5*" " + 0*"o" + "v")

print_tail_big()
print_body_big()
print_head_big()



# # ASCII Fish 

# print("   vvv")
# print("    v")
# print("   vov")
# print("  vooov")
# print(" vooooov")
# print("vooooooov") # size 1 -> 7 o's
# print(" voo oov")
# print("  v   v")

# # Bigger ASCII Fish

# print("    vvvvv")
# print("     vvv")
# print("      v")
# print("     vov")
# print("    vooov")
# print("   vooooov")
# print("  vooooooov")
# print(" vooooooooov")
# print("vooooooooooov") # size 2 -> 10 o's
# print(" voooo oooov")
# print("  voo   oov")
# print("   v     v")

