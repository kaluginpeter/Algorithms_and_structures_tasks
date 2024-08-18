# Imagine two arrays/lists where elements are linked by their positions in the array. For example:
#
# HowMany = [ 1   ,   6  ,  5  ,   0  ];
# Type = ['house', 'car','pen','jeans'];
# Means I have 1 house, 6 cars,5 pens and 0 jeans.
#
# Now if we sort one array we lose the connectivity.
# The goal is to create a sorting function that keeps
# the position link linkedSort(arrayToSort,linkedArray,compareFunction).
# So for every element that moves in arrayToSort(HowMany in the example),
# the corresponding element in linkedArray(Type in the example) needs to move similarly.
#
# For example in Javascript:
#
# //INPUT
# HowMany = [ 1   ,   6  ,  5  ,   0  ];
# Type = ['house', 'car','pen','jeans'];
#
# //SORT
# res = linkedSort(HowMany,Type,function(a,b){return a-b;})
#
# //OUTPUT
# HowMany === res === [ 0   ,   1   ,  5  ,  6  ];
# Type       ===     ['jeans','house','pen','car'];
# linkedSort(...) return the "arrayToSort" sorted only.
#
# If no compare function is provided you should handle like an alphabetical sorting would do, e.g:
#
# yoursortingfunction([-71,-6,35,0]) ===  [-6,-71,0,35] != [-71,-6,0,35]
# Note: it is assumed that array are same length.
#
# ARRAYSALGORITHMSSORTING
# Solution
def linked_sort(a_to_sort, a_linked, key=str):
    a_to_sort[:], a_linked[:] = zip(*sorted(zip(a_to_sort, a_linked), key=key))
    return a_to_sort