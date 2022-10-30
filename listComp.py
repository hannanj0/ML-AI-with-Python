# A program that uses list comprehension

names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0,
                             3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [estimated_cost * 11 /
                          10 for estimated_cost in estimated_insurance_costs]
total_cost = 0

for insurance_cost in actual_insurance_costs:
    total_cost += insurance_cost

average_cost = total_cost/len(actual_insurance_costs)

print("Average Insurance Cost: " + str(average_cost) + " dollars.")

for i in range(len(names)):
    name = names[i]
    insurance_cost = actual_insurance_costs[i]
    print("The insurance cost for " + name +
          " is " + str(insurance_cost) + " dollars.")

    if insurance_cost > average_cost:
        print("The insurance cost for " + name + " is above average.")
    elif insurance_cost < average_cost:
        print("The insurance cost for " + name + " is below average.")
    else:
        print("The insurance cost for " + name + " is equal to the average.")
