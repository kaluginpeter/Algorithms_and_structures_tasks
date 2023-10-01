# Write function bmi that calculates body mass index (bmi = weight / height2).
#
# if bmi <= 18.5 return "Underweight"
#
# if bmi <= 25.0 return "Normal"
#
# if bmi <= 30.0 return "Overweight"
#
# if bmi > 30 return "Obese"
#
# FUNDAMENTALS
# Solution
def bmi(weight, height):
    bmi_m = weight / height ** 2
    if bmi_m <= 18.5:
        return "Underweight"
    elif bmi_m <= 25.0:
        return "Normal"
    elif bmi_m <= 30.0:
        return "Overweight"
    elif bmi_m > 30:
        return "Obese"
