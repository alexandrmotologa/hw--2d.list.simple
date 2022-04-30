# 2 level list / bidimensional list
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

def errorInput():
    print("Value error")

# HW1: add the possibility to insert a value from kb
try:
    user_ri = int(input("Type a row (from 1 to 3): "))
    if user_ri >= 1 and user_ri <= 3:
        user_ci = int(input("Type a column (from 1 to 3): "))
        if user_ci >= 1 and user_ci <= 3:
            user_data = int(input("Type a new number: "))
            matrix[user_ri-1][user_ci-1] = user_data
            print()
            
            for ri in range(3):
                for ci in range(3):
                    print(matrix[ri][ci], end=" ")
                print()
        else:
            errorInput()
    else:
        errorInput()
except:
    errorInput()