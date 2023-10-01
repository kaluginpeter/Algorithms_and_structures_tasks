# Switch/Case - Bug Fixing #6
# Oh no! Timmy's evalObject function doesn't work. He uses Switch/Cases to evaluate the given properties of an object, can you fix timmy's function?
#
# DEBUGGING
# Solution
def eval_object(v):
    case = v["operation"]
    if case == "+":
        return v["a"] + v["b"]
    elif case == "-":
        return v["a"] - v["b"]
    elif case == "/":
        return v["a"] / v["b"]
    elif case == "*":
        return v["a"] * v["b"]
    elif case == "%":
        return v["a"] % v["b"]
    elif case == "**":
        return v["a"] ** v["b"]
    else:
        return 1