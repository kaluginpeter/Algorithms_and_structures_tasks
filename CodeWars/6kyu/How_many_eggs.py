# Ronald's uncle left him 3 fertile chickens in his will. When life gives you chickens, you start a business selling chicken eggs which is exactly what Ronald decided to do.
#
# A chicken lays 300 eggs in its first year. However, each chicken's egg production decreases by 20% every following year (rounded down) until when it dies (after laying its quota of eggs).
#
# After his first successful year of business, Ronald decides to buy 3 more chickens at the start of each year.
#
#
# Your Task:
#
# For a given year, and life span of chicken span, calculate how many eggs Ronald's chickens will lay him that year, whereby year=1 is when Ronald first got his inheritance and span>0.
#
# If year=0, make sure to return "No chickens yet!".
#
#
# Note:
#
# 1. All chickens have the same life span regardless of when they are bought.
# 2. Let's assume all calculations are made at the end of the year so don't bother taking eggs laid per month into consideration.
#
# 3. Each chicken's egg production goes down by 20% each year, NOT the total number of eggs produced by each 'batch' of chickens. While this might appear to be the same thing, it doesn't once non-integers come into play so take care that this is reflected in your kata!
#
# Algorithms
def egged(year, span):
    if not year:
        return 'No chickens yet!'
    total_eggs: int = 0
    coops: list[list[int, int]] = [[300, span], [300, span], [300, span]]
    for _ in range(year):
        total_eggs = 0
        coop_idx: int = 0
        while coop_idx < len(coops):
            outcome: int = coops[coop_idx][0]
            total_eggs += outcome
            coops[coop_idx][1] -= 1
            coops[coop_idx][0] = int(outcome - (outcome * 0.20))
            if not coops[coop_idx][1]:
                coops[len(coops) - 1], coops[coop_idx] = coops[coop_idx], coops[len(coops) - 1]
                coops.pop()
            else:
                coop_idx += 1
        coops.extend([[300, span], [300, span], [300, span]])
    return total_eggs