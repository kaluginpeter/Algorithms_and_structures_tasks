# Convert a hash into an array. Nothing more, Nothing less.
#
# {name: 'Jeremy', age: 24, role: 'Software Engineer'}
# should be converted into
#
# [["age", 24], ["name", "Jeremy"], ["role", "Software Engineer"]]
# Note: The output array should be sorted alphabetically by key name.
#
# Good Luck!
#
# ARRAYSLISTSFUNDAMENTALS
# Solution
def convert_hash_to_array(hash):
    return sorted([[k, v] for k,v in hash.items()])