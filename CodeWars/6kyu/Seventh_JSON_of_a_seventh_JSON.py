# Context
# According to Wikipedia : "The seventh son of a seventh son is a concept from folklore regarding special powers given to, or held by, such a son. The seventh son must come from an unbroken line with no female siblings born between, and be, in turn, born to such a seventh son."
#
# Your task
# You will be given a string of JSON, consisting of a family tree containing people's names, genders and children. Your task will be to find the seventh sons of seventh sons in the family tree, and return a set of their names. If there are none, return an empty set.
#
# Tips
# Have a good look at the sample test cases.
#
# For a seventh son to be a seventh son, there must not be any daughters in the line leading to him. There may be daughters after him, though.
#
# Use print_tree preloaded function to print the family tree in a compact human-readable form
#
# You may want to use the json module for this one.
#
# JSONRecursionFundamentals
# Solution
import json

def find_seventh_sons_of_seventh_sons(jstring: str) -> set:
    tree = json.loads(jstring)
    result = set()
    def dfs(node):
        children = node.get("children", [])
        sons = []
        for child in children:
            if child["gender"] == "male": sons.append(child)
            else: break
        if len(sons) >= 7:
            seventh_son = sons[6]
            grandsons = []
            for c in seventh_son.get("children", []):
                if c["gender"] == "male": grandsons.append(c)
                else: break
            if len(grandsons) >= 7: result.add(grandsons[6]["name"])
        for child in children:dfs(child)
    dfs(tree)
    return result