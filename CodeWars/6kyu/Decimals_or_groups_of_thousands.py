# Countries such as the U.S. and China use a dot to represent a decimal point, they also use a comma to seperate groups of thousands e.g. 4,353.56
#
# Other countries (mostly in Europe) instead use a comma to represent a decimal point, they also use a dot to seperate groups of thousands e.g. 4.353,56
#
# Your task is to sum up an array of string repensentation of numbers being in one of the two formats mentioned above with AT MOST two decimal places. The resulted sum should be a string with the format of xx,xxx.xx (keep two decimal places, seperate groups of thousands with comma if necessary)
#
# This Kata is inspired by one of the bugs that almost happened due to the differences in number formatting ( •̀ω•́ )σ
#
# Regular ExpressionsFundamentals
# Solution
from decimal import Decimal, getcontext

getcontext().prec = 30

def sum_up_numbers(numbers):
    total = Decimal("0")

    for num in numbers:
        if "." in num and "," in num:
            if num.rfind(",") > num.rfind("."):
                num = num.replace(".", "").replace(",", ".")
            else:
                num = num.replace(",", "")

        elif "," in num:
            parts = num.split(",")
            if len(parts[-1]) == 3:
                num = num.replace(",", "")
            else:
                num = num.replace(",", ".")

        elif "." in num:
            parts = num.split(".")
            if len(parts[-1]) == 3:
                num = num.replace(".", "")

        total += Decimal(num)

    return f"{total:,.2f}"