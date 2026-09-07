/*
Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (just like the name of this kata). Strings passed in will consist of only letters and spaces. Words will be separated by exactly one space. There will be no leading or trailing spaces.

Examples:

"Hey fellow warriors"  --> "Hey wollef sroirraw" 
"This is a test        --> "This is a test" 
"This is another test" --> "This is rehtona test"
StringsAlgorithms
*/
// Solution
package kata


func SpinWords(str string) string {
    var output []byte = make([]byte, 0)
    var i, n int = 0, len(str)
    for i < n {
        if i > 0 {
            output = append(output, ' ')
        }
        var tmp []byte = make([]byte, 0)
        for i < n && (str[i] != ' ') {
            tmp = append(tmp, str[i])
            i++
        }
        i++
        if (len(tmp) >= 5) {
            var left, right int = 0, len(tmp) - 1
            for left < right {
                var tmpByte byte = tmp[left]
                tmp[left] = tmp[right]
                tmp[right] = tmpByte
                left++
                right--
            }
        }
        output = append(output, tmp...)
    }
    return string(output)
}// SpinWords