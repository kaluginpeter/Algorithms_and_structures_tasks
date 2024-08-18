# Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses
#
# Examples
# balanced_parens(0) => [""]
# balanced_parens(1) => ["()"]
# balanced_parens(2) => ["()()","(())"]
# balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]
# ALGORITHMS
# Solution
def balanced_parens(n):
    output: list[str] = []

    def generate(n: int, left: int, right: int, comb: list[str]):
        if left >= n and right >= n:
            output.append(''.join(comb))
            return
        if left < n:
            comb.append('(')
            generate(n, left + 1, right, comb)
            comb.pop()
        if right < left:
            comb.append(')')
            generate(n, left, right + 1, comb)
            comb.pop()

    generate(n, 0, 0, [])
    return output