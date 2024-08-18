# Some people just have a first name; some people have first and last names and some people have first, middle and last names.
#
# You task is to initialize the middle names (if there is any).
#
# Examples
# 'Jack Ryan'                   => 'Jack Ryan'
# 'Lois Mary Lane'              => 'Lois M. Lane'
# 'Dimitri'                     => 'Dimitri'
# 'Alice Betty Catherine Davis' => 'Alice B. C. Davis'
# STRINGSFUNDAMENTALS
# Solution
def initialize_names(name):
    arr = name.split()
    l = []
    if len(arr)>2:
        l.append(arr[0])
        for i in arr[1:-1]:
            l.append(i[0].upper()+'.')
        l.append(arr[-1])
        return ' '.join(l)
    return name