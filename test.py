# Assignment 8
# 1. TileTraveller

# This assignment is to develop a computer game

# 9 reitir. Byrjar í reit 1,1 --> vilt enda í 3,1

# The player enters:
# n/N for north (up)
# e/E for east (right)
# s/S for south (down)
# w/W for west (left)

# Búa til fall/föll sem tekur inn strenginn direction_str og returnar réttum áttum sem notandi getur valið

# Kassi -- í hvaða átt
# 1,1 --> nN
# 1,2 --> nN, eE, sS
# 1,3 --> eE/sS
# 2,1 --> nN
# 2,2 --> sS/wW
# 2,3 --> wW/ eE
# 3,1 --> VICTORY
# 3,2 --> nN/ sS
# 3.3 --> wW /sS

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



# Kassi -- Í hvaða kassa lendiru
# # 1,1 -->nN --> 1,2

# 1,2: 
# eE --> 2,2
# nN --> 1,3
# sS --> 1,1
# 1,3:
# eE --> 2,3
# sS --> 1,2
# 2,1:
# nN --> 2,2
# 2,2:
# sS --> 2,1
# wW --> 1,2
# 2,3:
# wW --> 3,3
# eE --> 3,3
# 3,1 --> VICTORY
# 3,2:
# nN --> 3,3
# sS --> 3,1 
# 3.3:
# wW --> 2,3
# sS --> 3,2

# Norður/ Suður --> breyting á línu
# Austur / Vestur --> breyting á dálk

# Ef við förum austur þá hækkar dálkur um 1

# Ef við förum vestur þá lækkar dálkur um 1

# Ef við förum norður þá hækkar lína um 1

# Ef við förum suður þá lækkar lína um 1


# Strengir fyrir directions:
N = "(N)orth"
S = "(S)outh"
E = "(E)ast"
W = "(W)est"

print("You can travel: {}.".format(N)) # fyrsta print skipun, eina leiðin sem kemur til greina í 1,1
column = 1 # dálkur
row = 1 # lína

# Hugsum reitina sem línur og dálka. Dálkar liggja lóðrétt og línur lárétt.
# Hugsum reitina sem dálkur, lína 


def move_col_row(direction_str):

    direction_str = direction_str.lower() # breyti í lower því það má gera átt í hvorutveggja
    if direction_str == "n":
        row +=1
    elif direction_str == "s":
        row -= 1
    elif direction_str == "w":
        column += 1
    elif direction_str == "e":
        column -= 1 
    
    return column, row
    

direction_str = input("Direction: ")



