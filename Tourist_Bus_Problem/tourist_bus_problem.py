groups = [60, 10, 20, 50, 70, 40, 30, 10, 20]
capacity = 70
n = len(groups)
buses = range(n) # Possible bus indices (maximum one bus per group needed in worst case)
groups_idx = range(n)

import pulp

# Create the optimisation problem: minimise the number of buses used
model = pulp.LpProblem("Tourist_Bus_Problem", pulp.LpMinimize)

# Decision variables:
# x[i][j] = 1 if group i is assigned to bus j, 0 otherwise
x = pulp.LpVariable.dicts(
    "x",
    (groups_idx, buses),
    lowBound = 0, 
    upBound = 1,    
    cat = "Binary"  
)

# y[j] = 1 if bus j is used, 0 otherwise
y = pulp.LpVariable.dicts(
    "y",
    buses,
    lowBound = 0,  
    upBound = 1,   
    cat = "Binary" 
)

# Objective: Minimise the total number of buses used
model += pulp.lpSum(y[j] for j in buses)

# Constraint 1: Each group must be assigned to exactly one bus
for i in groups_idx:
    model += pulp.lpSum(x[i][j] for j in buses) == 1

# Constraint 2: The total number of tourists on each bus cannot exceed the bus capacity
for j in buses:
    model += (
        pulp.lpSum(groups[i] * x[i][j] for i in groups_idx)
        <= capacity * y[j]
    )

model.solve(pulp.PULP_CBC_CMD(msg=False))

print("Minimum number of buses:", pulp.value(model.objective))

for j in buses:
    if pulp.value(y[j]) == 1:
        assigned_groups = [
            groups[i] for i in groups_idx if pulp.value(x[i][j]) == 1
        ]
        print(f"Bus {j + 1}: {assigned_groups} -> total {sum(assigned_groups)}")