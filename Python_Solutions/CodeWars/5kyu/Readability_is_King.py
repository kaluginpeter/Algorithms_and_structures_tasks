# We will use the Flesch–Kincaid Grade Level to evaluate the readability of a piece of text. This grade level is an approximation for what schoolchildren are able to understand a piece of text. For example, a piece of text with a grade level of 7 can be read by seventh-graders and beyond.
#
# The way to calculate the grade level is as follows:
#
# (0.39 * average number of words per sentence) + (11.8 * average number of syllables per word) - 15.59
# Write a function that will calculate the Flesch–Kincaid grade level for any given string. Return the grade level rounded to two decimal points.
#
# Ignore hyphens, dashes, apostrophes, parentheses, ellipses and abbreviations.
#
# Remember that the text can contain more than one sentence: code accordingly!
#
# HINT: Count the number of vowels as an approximation for the number of syllables, but count groups of vowels as one (e.g. deal is one syllable). Do not count y as a vowel!
#
# Example
# "The turtle is leaving." ==> 3.67
# The average number of words per sentence is 4 and the average number of syllables per word is 1.5. The score is then (0.39 * 4) +  (11.8 * 1.5) - 15.59 = 3.67
#
# MATHEMATICSALGORITHMS
# Solution
def flesch_kincaid(text):
    sentences: list[str] = [text]
    for sep in '!?.':
        after_sep: list[str] = []
        for seq in sentences:
            after_sep.extend([i for i in seq.split(sep) if i])
        sentences = after_sep

    sillables: list[int] = []
    average_words: float = sum(len(seq.split()) for seq in sentences) / len(sentences)
    for sentence in sentences:
        for word in sentence.split():
            sillable: int = 0
            char: int = 0
            flag: bool = False
            while char < len(word):
                if word[char] in 'AEOIUaeoiu':
                    if flag:
                        char += 1
                    else:
                        sillable += 1
                        flag = True
                else:
                    char += 1
                    flag = False
            sillables.append(sillable)

    average_sillables: float = sum(sillables) / len(sillables)
    return round((0.39 * average_words) + (11.8 * average_sillables) - 15.59, 2)