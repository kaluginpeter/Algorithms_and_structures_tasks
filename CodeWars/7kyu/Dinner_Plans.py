# Two samurai generals are discussing dinner plans after a battle, but they can't seem to agree.
# The discussion gets heated and you are cannot risk favoring either of them as this might damage your political standing with either of the two clans the samurai generals belong to. Thus, the only thing left to do is find what the common ground of what they are saying is.
#
# Compare the proposals with the following function:
#
# def common_ground(s1,s2)
# The parameters s1 and s2 are the strings representing what each of the generals said. You should output a string containing the words in s1 that also occur in s2.
#
# Each word in the resulting string shall occur once, and the order of the words need to follow the order of the first occurence of each word in s2.
#
# If they are saying nothing in common, kill both samurai and blame a ninja. (output "death")
#
# StringsArraysFundamentals
# Solution
def common_ground(s1,s2):
    hashmap: dict[str, int] = dict()
    output: list[str] = []
    idx: int = 0
    for word in s2.split():
        if word not in hashmap:
            hashmap[word] = idx
        idx += 1
    for word in set(s1.split()):
        if word in hashmap:
            output.append(word)
    output.sort(key=lambda word: hashmap[word])
    return ' '.join(output) if output else 'death'