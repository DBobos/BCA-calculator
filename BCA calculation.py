from sympy import symbols, solve
import math
# # Define the variables
# x, y = symbols('x y')

# # Given value for y
# y_value = 9.8775

#   # Example value for y

# # Define the equation
# equation = x - (x/4 + y)

# # Solve the equation for x
# solution = solve(equation.subs(y, y_value), x)

# # Filter solutions to ensure x > 0

# for sol in solution:
#     if sol > 0:
#         print(sol)
#     else: pass

# positive_solutions = [sol for sol in solution if sol > 0]

# # Display the solution
# print("The solution for x - (x/4 + y) with y =", y_value, "and x > 0 is:")

# for val in positive_solutions:
#     print("Original value for total where H20 is 0",(val), end=' ')
#     print("Rounded up value to closer integer",math.ceil(val), end=' ')



################# find the minimum dye amount and solve ###################################################### 
def find_x_1st(y):
    # Rearranging the inequality: x > 4y / 3
    return (4 * y) / 3


################# find solving for Total given the dye amount ###################################################### 
def find_x(y, dye):
    # Rearranging the inequality: x > f + y
    return dye + y


def get_concentration(protein,y):
    return protein / y
# asking for 30μg/μL protein
# y = input("Enter the amount for 30μg/μL protein : ")
# y = float(y)
  # You can change this value

# x_min = math.ceil(find_x_1st(y))
# print(f"The minimum rounded up value of Total that satisfies the inequality is: {x_min}")


#### set dye amount is Total / 4 ########################

# dye = x_min / 4 
# print(f"The dye amount is: {dye}")

###### change if dye amount has to be different ################
# while True:
#     user_input = input("Do you want to change the dye amount calculated? {dye}? (yes/no): ")
#     if user_input.lower() in ["yes", "y"]:
#         dye= int(input("Enter the dye amount : "))
        
#         break
#     elif user_input.lower() in ["no", "n"]:
#         break
#     else:
#         print("Invalid input. Please enter yes/no.")


concentration = input("Enter the amount of protein per μL eg. 20 for 20μg/μL protein : ")
concentration = float(concentration)
###### BCA Calculating  ################
while True:
    user_input = input("Do you  know the dye amount? (yes/no): ")
    if user_input.lower() in ["yes", "y"]:
        y = input("Enter the Concentration μg/μl protein : ")
        y = get_concentration(concentration, float(y))
        print(f"your protein per: {concentration} ")
        print(f"μg/μL is: {y}")
        x_min_2_original = find_x(y, dye)
        x_min_2 = math.ceil(find_x(y, dye))
        print(f"The minimum value of Total that satisfies the inequality is: {x_min_2_original}")
        print(f"The minimum rounded up value of Total that satisfies the inequality is: {x_min_2}")
        user_input = input("Do you want to continue? (yes/no): ")
        if user_input.lower() in ["yes", "y"]:
            pass
        elif user_input.lower() in ["no", "n"]:
          exit()
    elif user_input.lower() in ["no", "n"]:
        user_input = input("Do you  want to calculate the dye amount? (yes/no): ")
        if user_input.lower() in ["yes", "y"]:
            y = input("Enter the Concentration μg/μl protein : ")
            y = get_concentration(concentration, float(y))
            print(f"your protein per: {concentration} ")
            print(f"μg/μL is: {y}")
            x_min_original = find_x_1st(y)
            x_min = math.ceil(find_x_1st(y))
            print(f"The minimum value of Total that satisfies the inequality is: {x_min}")
            print(f"The minimum rounded up value of Total that satisfies the inequality is: {x_min}")
            dye = x_min / 4
            print(f"The dye amount is: {dye}")
        elif user_input.lower() in ["no", "n"]:
            dye =float(input("Enter the amount for dye : "))
            print(f"dye is set to {dye}")
        
        



# # change the y
# y = input("Enter the amount for 30μg/μL protein : ")
# y = float(y)

# x_min_2 = math.ceil(find_x(y, dye))
# print(f"The minimum rounded up value of Total that satisfies the inequality is: {x_min_2}")