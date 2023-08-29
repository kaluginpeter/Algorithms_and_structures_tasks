# This is the first part of this kata series. Second part is here and third part is here
#
# Add two English words together!
#
# Implement a class Arith (struct struct Arith{value : &'static str,} in Rust) such that
#
#   //javascript
#   var k = new Arith("three");
#   k.add("seven"); //this should return "ten"
# Input - Will be between zero and ten and will always be in lower case
#
# Output - Word representation of the result of the addition. Should be in lower case
#
# MATHEMATICSFUNDAMENTALS
# Solution
integer = ['zero', 'one', 'two', 'three', 'four', 'five',
           'six', 'seven', 'eight', 'nine', 'ten','eleven',
           'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
           'seventeen', 'eighteen', 'nineteen', 'twenty']
class Arith():
    def __init__(self, int):
        self.i = integer.index(int)
    def add(self, int):
         return integer[integer.index(int) + self.i]