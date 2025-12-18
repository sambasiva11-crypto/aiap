# Import PuLP library
from pulp import LpMaximize, LpProblem, LpVariable, value

# Create the linear programming problem
prob = LpProblem("Chocolate_Profit_Maximization", LpMaximize)

# Decision variables: number of units to produce for A and B
A = LpVariable('A', lowBound=0, cat='Continuous')  # Units of chocolate A
B = LpVariable('B', lowBound=0, cat='Continuous')  # Units of chocolate B

# Objective function: Maximize profit
prob += 6 * A + 5 * B, "Total_Profit"

# Constraints
prob += A + B <= 5, "Milk_Constraint"      # 5 units of milk available
prob += 3 * A + 2 * B <= 12, "Choco_Constraint"  # 12 units of choco available

# Solve the problem
prob.solve()

# Output results
print("Status:", prob.status)
print("Optimal production of A:", value(A))
print("Optimal production of B:", value(B))
print("Maximum Profit:", value(prob.objective))
