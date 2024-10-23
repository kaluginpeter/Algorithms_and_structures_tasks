# Many people love dogs. Also, many people have or have had a dog, and would want to get a new dog with a similar personality as their current or previous dog, but they don't know where to look. Thankfully, you are here to help.
#
#
# Your task in this kata is to implement a dog recommendation system. You will be given the name of a dog breed (as a string), for which you will have to return a set of the breeds that are most similar to this breed in temper (excluding itself). To aid you in this task, you are given a dictionary, dogs, mapping dog breeds (e.g., "Chihuahua") to a set of adjectives describing that breed's typical temperament (e.g., {"Lively", "Devoted", "Courageous", "Alert", "Quick"}). The dictionary is preloaded, so you may access it as if you had defined it in your own code.
#
# To be clear, two breeds are more similar in temper the more adjectives they share. For example, if dog breed A has adjectives {"Lively", "Devoted"}, it is more similar to dog breed B ({"Lively", "Devoted"}, two adjectives in common) than to dog breed C ({"Lively", "Alert"}, one adjective in common) or even dog breed D ({"Alert", "Quick"}, zero adjectives in common). If one breed has more adjectives in common with the original breed than any other, return a set containing only this breed. If more than one breed has the same number of adjectives in common with the original breed, return a set of these breeds.
#
# Dog breeds taken here. Dog temperaments taken from Google (search, e.g., "Chihuahua temperament").
#
# ARRAYSSETSSORTINGFUNDAMENTALS
# Solution
def find_similar_dogs(breed):
    needed: set[str] = dogs[breed]
    hashmap: dict[str, int] = dict()
    max_matching: int = 0
    for dog in dogs:
        if dog == breed: continue
        matching: int = len(dogs[dog] & needed)
        hashmap[dog] = matching
        max_matching = max(max_matching, matching)
    output: set[str] = set()
    for dog in hashmap:
        if hashmap[dog] == max_matching:
            output.add(dog)
    return output