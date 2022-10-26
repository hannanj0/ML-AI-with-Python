# A program that takes different factors and finds out how it influences medical costs
# Hannan Jawad

# create the initial variables below
age = 28
smoker = 0
sex = 0
bmi = 26.2
num_of_children = 3

insurance_cost = 250 * age - 128 * sex + 370 * bmi + \
    425 * num_of_children + 24000 * smoker - 12500

print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

# Age Factor
age += 4
new_insurance_cost = 250 * age - 128 * sex + 370 * \
    bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in cost of insurance after increasing the age by 4 years is " +
      str(change_in_insurance_cost) + " dollars.")

age = 28

# BMI Factor
bmi += 3.1
new_insurance_cost = 250 * age - 128 * sex + 370 * \
    bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated insurance cost after increasing BMI by 3.1 is " +
      str(change_in_insurance_cost) + " dollars.")

bmi = 26.2

# Male vs. Female Factor
sex = 1

new_insurance_cost = 250 * age - 128 * sex + 370 * \
    bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being male instead of female is " +
      str(change_in_insurance_cost) + " dollars.")

sex = 0

# Extra Practice
# Smoker vs. Non Smoker
smoker = 1

new_insurance_cost = 250 * age - 128 * sex + 370 * \
    bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being a smoker instead of a non smoker is " +
      str(change_in_insurance_cost) + " dollars.")

smoker = 0

# Children vs. no children
num_of_children = 0

new_insurance_cost = 250 * age - 128 * sex + 370 * \
    bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for having children compared to no children is " +
      str(change_in_insurance_cost) + " dollars.")

num_of_children = 3
