/*
The book "Guide to Teaching Puzzle-based Learning" includes the following puzzle:

"A boy sometimes misses the bus. The bus is supposed to leave at 8:00, but it arrives at the stop some time between 7:58 and 8:02 and departs immediately once everyone is on board. The boy tries to reach the stop early, but due to various circumstances he arrives some time between 7:55 and 8:01. How often does the boy miss the bus?" (Text edited for brevity.) The book explains how to find the solution, which is 18.75%.

Let's solve this problem in general. Inputs are the bus range first, followed by the boy range. Both ranges are tuples (or lists or arrays, depending on language) of two elements; the second time is guaranteed to be later than the first. The bus and boy are equally likely to arrive at any time in their range. You don't have to take into account the time that the bus waits - assume people board the bus instantly :-). The boy makes the bus only if he arrives before or at the moment it does. Compute how often the boy misses the bus, as a percentage.

Times are given as strings containing hour, minute, and AM/PM. Example: (("7:58 AM", "8:02 AM"), ("7:55 AM", "8:01 AM")) should return 18.75 Answers are accepted if within 0.001 of the solution.

Note: The bus runs between 2am and 11pm. The boy's times will be sufficiently close to the bus times so that calculating across to the previous or next day is not needed.

Also check out Catch the Bus - Continuous Edition

ProbabilityDate TimeGeometry
*/
// Solution
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <utility>
int parseTimeToMinutes(const std::string& timeStr) {
    int hours, minutes;
    char ampm_chars[3];
    if (std::sscanf(timeStr.c_str(), "%d:%d %2s", &hours, &minutes, ampm_chars) != 3) return -1;
    std::string ampm(ampm_chars);
    if (ampm == "AM") {
        if (hours == 12) hours = 0;
    } else if (ampm == "PM") {
        if (hours != 12) hours += 12;
    }
    return hours * 60 + minutes;
}

double catchTheBus(std::pair<std::string, std::string> busTimes,
                   std::pair<std::string, std::string> boyTimes) {
    double b_s = static_cast<double>(parseTimeToMinutes(busTimes.first));
    double b_e = static_cast<double>(parseTimeToMinutes(busTimes.second));
    double p_s = static_cast<double>(parseTimeToMinutes(boyTimes.first));
    double p_e = static_cast<double>(parseTimeToMinutes(boyTimes.second));
    double D_b = b_e - b_s;
    double D_p = p_e - p_s;
    if (D_b <= 0 || D_p <= 0) {
        if (p_s >= b_e) return 100.0;
        if (p_e <= b_s) return 0.0;
    }
    double totalSampleArea = D_b * D_p;
    std::vector<double> critical_points;
    critical_points.push_back(b_s);
    critical_points.push_back(b_e);
    if (p_s > b_s && p_s < b_e) critical_points.push_back(p_s);
    if (p_e > b_s && p_e < b_e) critical_points.push_back(p_e);
    std::sort(critical_points.begin(), critical_points.end());
    critical_points.erase(std::unique(critical_points.begin(), critical_points.end()), critical_points.end());
    double areaCatch = 0.0;
    for (size_t i = 0; i < critical_points.size() - 1; ++i) {
        double t1 = critical_points[i];
        double t2 = critical_points[i+1];
        if (t1 >= t2) continue;
        double val_at_t1 = std::max(0.0, std::min(p_e, t1) - p_s);
        double val_at_t2 = std::max(0.0, std::min(p_e, t2) - p_s);
        areaCatch += (val_at_t1 + val_at_t2) / 2.0 * (t2 - t1);
    }

    double probCatch = 0.0;
    if (totalSampleArea > 1e-9) {
        probCatch = areaCatch / totalSampleArea;
    } else {
        if (p_e <= b_s) probCatch = 1.0;
        else if (p_s >= b_e) probCatch = 0.0;
    }


    double probMiss = 1.0 - probCatch;
    probMiss = std::max(0.0, std::min(1.0, probMiss));

    return probMiss * 100.0;
}
