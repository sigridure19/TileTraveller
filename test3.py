# Mögulegar direction fyrir hvern kassa
# Kassi [1,1]       Kassi[1,2]         Kassi[1,3]
# North             North              East
#                   East               South
#                   South

# Kassi [2,1]       Kassi[2,2]          Kassi[2,3]
# North             South               East
#                   West                West
#

# Kassi [3,1]       Kassi[3,2]         Kassi[3,3]
# VICTORY           North              South
#                   South              West

# Gerum fall fyrir hvern reit fyrir sig.


# Strengir fyrir directions:
N = "(N)orth"
E = "(E)ast"
S = "(S)outh"
W = "(W)est"



def box_1_1():
    print("You can travel: {}".format(N))
    direction_str = input("Direction: ").lower()
    if direction_str == "n":
        return box_1_2
    else:
        print("Not a valid direction!")
        return box_1_1

def box_1_2():
    print("You can travel: {} or {} or {}.".format(N,E,S))
    direction_str = input("Direction: ").lower()
    if direction_str == "n":
        return box_1_3
    elif direction_str == "e":
        return box_1_2
    elif direction_str == "s":
        return box_1_1
    else:
        print("Not a valid direction!")
        return box_1_2

def box_2_2():
    print("You can travel: {} or {}.".format(S,W))
    direction_str = input("Direction: ").lower()
    if direction_str == "s":
        return box_2_1
    elif direction_str == "w":
        return box_1_2
    else:
        print("Not a valid direction!")
        return box_2_2

def box_2_1():
    print("You can travel: {}".format(N))
    direction_str = input("Direction: ").lower()
    if direction_str == "n":
        return box_2_2
    else:
        print("Not a valid direction!")
        return box_2_1

def box_1_3():
    print("You can travel: {} or {}.".format(E,S))
    direction_str = input("Direction: ").lower()
    if direction_str == "e":
        return box_2_3
    elif direction_str == "s":
        return box_1_2
    else:
        print("Not a valid direction!")
        return box_1_3

def box_2_3():
    print("You can travel: {} or {}.".format(E,W))
    direction_str = input("Direction: ").lower()
    if direction_str == "e":
        return box_3_3
    elif direction_str == "w":
        return box_1_3
    else:
        print("Not a valid direction!")
        return box_2_3

def box_3_3():
    print("You can travel: {} or {}.".format(S,W))
    direction_str = input("Direction: ").lower()
    if direction_str == "s":
        return box_3_2
    elif direction_str == "w":
        return box_2_3
    else:
        print("Not a valid direction!")
        return box_3_3

def box_3_2():
    print("You can travel: {} or {}.".format(N,S))
    direction_str = input("Direction: ").lower()
    if direction_str == "n":
        return box_3_3
    elif direction_str == "s":
        return box_3_1
    else:
        print("Not a valid direction!")
        return box_3_2
    
def box_3_1():
    print("Victory!")