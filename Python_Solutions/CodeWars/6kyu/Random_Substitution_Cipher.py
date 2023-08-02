# Most substitution ciphers involve the use of a shift value. The simplest ones apply the same shift value to all letters. Some are slightly more sophisticated, but there is still a consistent rule governing the shift.
#
# This kata is different. Your task here is to create a random substitution cipher.
#
# There is no input to the function. The output from your code should be an object in which the keys are simply all the letters of the English alphabet, in lower case and in alphabetical order. The value of each key will also be a lower-case letter, which you should select at random. Because it is random, it is also possible that the original letter and the substituted letter will be the same, as you can see in the following example of possible output:
#
# {"a":"c", "b":"p", "c":"j", "d":"a", "e":"v", "f":"d", "g":"g", "h":"u", "i":"l", "j":"t", "k":"n", "l":"w", "m":"m", "n":"o", "o":"i", "p":"s", "q":"f", "r":"r", "s":"x", "t":"b", "u":"h", "v":"y", "w":"q", "x":"e", "y":"k", "z":"z"}
#
# The output from your solution will be tested for a high probability of randomness. Special thanks to @halcarleton and @Vaults for showing me how to do this. There might be a clever way to cheat, but where's the fun in that?
#
# FUNDAMENTALS
# Solution
import random
def random_sub():
    d = {"a":"c", "b":"p", "c":"j", "d":"a", "e":"v", "f":"d",
         "g":"g", "h":"u", "i":"l", "j":"t", "k":"n", "l":"w",
         "m":"m", "n":"o", "o":"i", "p":"s", "q":"f", "r":"r", "s":"x", "t":"b",
         "u":"h", "v":"y", "w":"q", "x":"e", "y":"k", "z":"z"}
    en_al = 'abcdefghijklmnopqrstuvwxyz'
    for k, v in d.items():
        let = random.choice(en_al)
        d[k] = let
        en_al = en_al.replace(let, '')
    return d