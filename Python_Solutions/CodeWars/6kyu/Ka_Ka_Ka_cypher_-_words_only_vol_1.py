# Introduction
# Ka ka ka cypher is a cypher used by small children in some country.
# When a girl wants to pass something to the other girls and there are some boys nearby,
# she can use Ka cypher. So only the other girls are able to understand her.
# She speaks using KA, ie.:
# ka thi ka s ka bo ka y ka i ka s ka u ka gly what simply means this boy is ugly.
#
# Task
# Write a function that accepts a string word and returns encoded message using ka cypher.
#
# Our rules:
#
# The encoded word should start from ka.
# The ka goes after vowel (a,e,i,o,u)
# When there is multiple vowels together, the ka goes only after the last vowel
# When the word is finished by a vowel, do not add the ka after
# Input/Output
# The word string consists of only lowercase and uppercase characters.
# There is only 1 word to convert - no white spaces.
#
# Example
# "a" => "kaa"
# "ka" => "kaka"
# "aa" => "kaaa"
# "Abbaa" => "kaAkabbaa"
# "maintenance" => "kamaikantekanakance"
# "Woodie" => "kaWookadie"
# "Incomprehensibilities" => "kaIkancokamprekahekansikabikalikatiekas"
# Remark
# Ka cypher's country residents, please don't hate me for simplifying the
# way how we divide the words into "syllables" in the Kata. I don't want to make it too hard for other nations ;-P
#
# FUNDAMENTALS
# Solution
def ka_co_ka_de_ka_me(word):
    w = ""
    for k, v in enumerate(word):
        if k != len(word):
            if v.lower() not in "aeiou" and word[k-1].lower() in "aeiou" and k != 0: w += "ka"
        w += v
    return "ka" + w