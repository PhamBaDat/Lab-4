from pprint import pprint
from itertools import combinations
import math

# List of items (name, size, value)
items = {
    'r': ('rifle', 3, 25),
    'p': ('pistol', 2, 15),
    'a': ('ammo', 2, 15),
    'm': ('medkit', 2, 20),
    'i': ('inhaler', 1, 5),  # Mandatory / астма
    'k': ('knife', 1, 15),
    'x': ('axe', 3, 20),
    't': ('talisman', 1, 25),
    'f': ('flask', 1, 15),
    'd': ('antidot', 1, 10), # заражение
    's': ('supplies', 2, 20),
    'c': ('crossbow', 2, 20),
}

# def table_memo(items, max_cells):
#     table = [[ 0 for _ in range (max_cells)] for _ in range(len(items))]
#     for row, value in enumerate(items.values()):
#         cells = value['cell']
#         price = value['price']
#         for limit_cells in range(1, max_cells+1):
#             col = limit_cells - 1

#             if row == 0:
#                 table[row][col] = 0 if cells > limit_cells else price
#             else:
#                 prev_price = table[row-1][col]
#                 if cells > limit_cells:
#                     used = 0 if col - cells < 0 else table[row-1][col-cells]
#                     res = max([prev_price, price + used])
#                     table[row][col] = res
#     pprint(table)

def Optimal_Choice():
    pack = ['d']
    space = MAX_CELLS - items['i'][1]

    # Prepare assist Lists
    items_left = [item for item in items if item!='i']
    sizes =  [items[item][1] for item in items_left]
    values = [items[item][2] for item in items_left]

    # Create Table Dynamic Programming
    table_dp = [[0] * (space+1) for _ in range(len(items) + 1)]
    for i in range (len(items_left)):
        for j in range (space + 1):
            table_dp[i+1][j] =  table_dp[i][j]
            if j>= sizes[i]:
                table_dp[i+1][j] = max(table_dp[i+1][j], table_dp[i][j - sizes[i]] + values[i])
    
    # Trace back to get list items
    space_left = space
    for i  in range(len(items_left), 0, -1):
        if table_dp[i][space_left] != table_dp[i-1][space_left]:
            pack.append(items_left[i-1])
            space_left -= sizes[i-1]

    # Sort backpack to 3x3
    backpack = [["" for _ in range(4)] for _ in range(2)]
    a = 0
    for item in pack:
        s = items[item][1]
        while s != 0:
            row = a // 4
            col = a % 4
            backpack[row][col] = f'[{item}]'
            a+=1
            s-=1

    print ("Backpack:")
    for row in backpack:
        print(" ".join(row))    

    # Calculate Total survival points!
    minus_points = 0
    total_points = Beginner_survival_point
    for item in pack:
        total_points += items[item][2]
        if item not in pack:
            minus_points += items[item][2]
    print (f'Total survival points: {total_points - minus_points}')

def Small_backpack():
    CELLS = 7
    list = []

    for a in range(1, n+1):
        for comb in combinations(items.keys(), a):
            if 'i' in comb:
                total_space = 0
                total_point = 0
                minus_point = 0

                for item in comb:
                    total_space += items[item][1]
                    total_point += items[item][2]
                for item in items:
                    if item not in comb:
                        minus_point += items[item][2]

                sum = total_point - minus_point
                if  total_space <= CELLS and sum > 0:
                    list.append((comb, sum))

    print("Small Backpack Combination:")
    if list!=[]:
        for i, (comb, sum) in enumerate(list, 1):
            print(f"Combination {i} : {list} - Survival points: {sum}")
    else:
        print("-> No valid combinations found.")



if __name__ == '__main__':
    MAX_CELLS = 8
    Beginner_survival_point = 20
    n = len(items)

    Optimal_Choice()
    Small_backpack()