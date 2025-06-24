/*
Kata Task
You are given a list of cogs in a gear train

Each element represents the number of teeth of that cog

e.g. [100, 75] means

1st cog has 100 teeth
2nd cog has 75 teeth
If the first cog rotates clockwise at 1 RPM what is the RPM of the final cog?

(use negative numbers for anti-clockwise rotation)

Notes
no two cogs share the same shaft
Series:

Cogs
Cogs 2
Fundamentals
*/
// Solution
double cog_rpm(const std::vector<int>& cogs)
{
    if (cogs.empty()) return 0.0;
    if (cogs.size() == 1) return 1.0;
    double direction_multiplier = (cogs.size() % 2 == 0) ? -1.0 : 1.0;
    double speed_ratio = static_cast<double>(cogs.front()) / cogs.back();
    return speed_ratio * direction_multiplier;
}