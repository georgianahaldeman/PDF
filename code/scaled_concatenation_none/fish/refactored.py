
def print_tail(size):
    spaces_count = size+2
    for v_count in range(2*size+1,0,-2):
        print(spaces_count*" " + v_count*"v")
        spaces_count += 1

def print_body(size):
    spaces_count = 2*size+1
    for o_count in range(1,4*(size+1),2):
        print(spaces_count*" " + "v" +o_count* "o" + "v")
        spaces_count -= 1


def print_head(size):
    spaces_count = 1
    middle_spaces = 1
    for o_count in range(2*size,-1,-2):
        print(spaces_count*" " + "v" + o_count*"o" + middle_spaces*" " + o_count*"o" + "v")
        spaces_count += 1
        middle_spaces += 2

def print_fish(size=1):
    print_tail(size)
    print_body(size)
    print_head(size)

print_fish(1)
print_fish(2)