
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

#FALLIÐ 

def move_col_row(direction_str):
    direction_str = direction_str.lower() # breyti í lower því það má gera átt í hvorutveggja
    col = 1 # dálkur
    row = 1 # lína
    if direction_str == "n":
        row +=1
    elif direction_str == "s":
        row -= 1
    elif direction_str == "w":
        col += 1
    elif direction_str == "e":
        col -= 1 
    
    return col, row


# Strengir fyrir directions:
N = "(N)orth"
E = "(E)ast"
S = "(S)outh"
W = "(W)est"

 # fyrsta print skipun, eina leiðin sem kemur til greina í 1,1

direction_str = input("Direction: ")
col, row = move_col_row(direction_str)
print(col, row)

while 
if 0 >= col <= 4 or 0>= row <= 4:
    print("Not a valid direction!")
    
if col == 1 and row == 1:
    print("You can travel: {}".format(N))

if col == 1 and row == 2:
    print("You can travel: {} or {} or {}.".format(N,E,S))

if (col == 2 and row == 2) or (col == 3 and row == 3):
    print("You can travel: {} or {}.".format(S,W))

if col == 2 and row == 1:
    print("You can travel: {}.".format(N))

if col == 1 and row == 3:
    print("You can travel: {} or {}.".format(E,S))

if col == 2 and row == 3:
    print("You can travel: {} or {}.".format(E,W))

if col == 3 and row == 2:
    print("You can travel: {} or {}.".format(N,S))

if col == 3 and row ==1:
    print("Victory!")


    