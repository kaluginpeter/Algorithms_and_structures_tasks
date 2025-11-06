/*
UTF-8 is a Unicode encoding. It is by far the dominant encoding for webpages, and is in widespread use for storing text files on disk or exchanging textual data between computers or programs.

UTF-8 is a variable-length encoding: the representation of a codepoint can take from 1 to 4 8-bit code-units , depending on the codepoint's numerical value.

The Problem
In languages where "strings" are really sequences of 8-bit bytes (C/C++, PHP, OCaml, Lua...), UTF-8 is a possible encoding for them and usually has some level of language support. However, the function/method/property to retrieve the string's length actually returns the number of bytes in the string, not the number of codepoints.

For example
The codepoint of the emoji 🙉 (U+1F649, Hear-No-Evil Monkey) is 0x1F649.

std::string(u8"🙉").length() // 4
Task
Write a function that returns the number of codepoints in a UTF-8 string.

""        --> 0
"Aÿ♠🙉"  --> 4
"é"       --> 1 (actual é character)
"é"       --> 2 (e + combining acute accent)
"㐷©∏!重" --> 5
See also
Same task but in UTF-16, also a variable-length Unicode encoding.

StringsUnicode
*/
// Solution
#include <string>
#include <cstddef>

std::size_t CountCodepoints(const std::string &utf8)
{
    size_t output = 0;
    for (const char& ch : utf8) {
        if ((ch & 0b11000000) != 0b10000000) ++output;
    }
    return output;
}