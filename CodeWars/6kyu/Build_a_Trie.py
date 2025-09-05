# The goal of this kata is to implement trie (or prefix tree) using dictionaries (aka hash maps or hash tables), where:
#
# the dictionary keys are the prefixes
# the value of a leaf node is None in Python, nil in Ruby, null in Groovy, JavaScript and Java, and Nothing in Haskell.
# the value for empty input is {} in Python, Ruby, Javascript and Java (empty map), [:] in Groovy, and Trie [] in Haskell.
# Examples:
#
# >>> build_trie()
# {}
# >>> build_trie("")
# {}
# >>> build_trie("trie")
# {'t': {'tr': {'tri': {'trie': None}}}}
# >>> build_trie("tree")
# {'t': {'tr': {'tre': {'tree': None}}}}
# >>> build_trie("A","to", "tea", "ted", "ten", "i", "in", "inn")
# {'A': None, 't': {'to': None, 'te': {'tea': None, 'ted': None, 'ten': None}}, 'i': {'in': {'inn': None}}}
# >>> build_trie("true", "trust")
# {'t': {'tr': {'tru': {'true': None, 'trus': {'trust': None}}}}}
# Happy coding! :)
#
# Data StructuresFundamentals