/*
Introduction
In the United Kingdom, the driving licence is the official document which authorises its holder to operate various types of motor vehicle on highways and some other roads to which the public have access. In England, Scotland and Wales they are administered by the Driver and Vehicle Licensing Agency (DVLA) and in Northern Ireland by the Driver & Vehicle Agency (DVA). A driving licence is required in the UK by any person driving a vehicle on any highway or other road defined in s.192 Road Traffic Act 1988[1] irrespective of ownership of the land over which the road passes, thus including many which allow the public to pass over private land; similar requirements apply in Northern Ireland under the Road Traffic (Northern Ireland) Order 1981. (Source Wikipedia)
Driving
Task
The UK driving number is made up from the personal details of the driver. The individual letters and digits can be code using the below information
Rules
1–5: The first five characters of the surname (padded with 9s if less than 5 characters)

6: The decade digit from the year of birth (e.g. for 1987 it would be 8)

7–8: The month of birth (7th character incremented by 5 if driver is female i.e. 51–62 instead of 01–12)

9–10: The date within the month of birth

11: The year digit from the year of birth (e.g. for 1987 it would be 7)

12–13: The initial letter of the first name and middle name, padded with a 9 if no middle name

14: Arbitrary digit – usually 9, but decremented to differentiate drivers with the first 13 characters in common. We will always use 9

15–16: Two computer check digits. We will always use "AA"
Your task is to code a UK driving license number using an Array of data. The Array will look like

data = {"John","James","Smith","01-Jan-2000","M"};
Where the elements are as follows

0 = Forename
1 = Middle Name (if any)
2 = Surname
3 = Date of Birth (In the format Day Month Year, this could include the full Month name or just shorthand ie September or Sep)
4 = M-Male or F-Female
You will need to output the full 16 digit driving license number, in all UPPERCASE.

Good luck and enjoy!

Kata Series
If you enjoyed this, then please try one of my other Katas. Any feedback, translations and grading of beta Katas are greatly appreciated. Thank you.
*/
//Solution
#include <string>
#include <array>
#include <vector>
#include <map>
#include <algorithm>
#include <cctype>

using namespace std;

string driver(const array<string, 5> &data)
{
    static const map<string, int> month_to_int = {
        {"Jan", 1}, {"January", 1}, {"Feb", 2}, {"February", 2},
        {"Mar", 3}, {"March", 3},   {"Apr", 4}, {"April", 4},
        {"May", 5},                 {"Jun", 6}, {"June", 6},
        {"Jul", 7}, {"July", 7},    {"Aug", 8}, {"August", 8},
        {"Sep", 9}, {"September", 9},{"Oct", 10},{"October", 10},
        {"Nov", 11},{"November", 11},{"Dec", 12},{"December", 12}
    };
    string license_number = "";
    string surname = data[2];
    if (surname.length() >= 5) license_number += surname.substr(0, 5);
    else {
        license_number += surname;
        while (license_number.length() < 5) license_number += '9';
    }
    const string& dob_str = data[3];
    size_t first_dash = dob_str.find('-');
    size_t second_dash = dob_str.find('-', first_dash + 1);
    string day_part = dob_str.substr(0, first_dash);
    string month_part = dob_str.substr(first_dash + 1, second_dash - (first_dash + 1));
    string year_part = dob_str.substr(second_dash + 1);
    license_number += year_part[2];
    int month_val = month_to_int.at(month_part);
    if (data[4] == "F") month_val += 50;
    string month_str = to_string(month_val);
    if (month_str.length() == 1) license_number += "0";
    license_number += month_str;
    if (day_part.length() == 1) license_number += "0";
    license_number += day_part;
    license_number += year_part[3];
    license_number += data[0][0];
    if (!data[1].empty()) license_number += data[1][0];
    else license_number += '9';
    license_number += '9';
    license_number += "AA";
    transform(license_number.begin(), license_number.end(), license_number.begin(), ::toupper);
    return license_number;
}