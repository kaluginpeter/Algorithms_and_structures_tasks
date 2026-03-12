/*
The King and Queen of FarFarAway are going to pay Shrek and Fiona a visit at their swamp. However, Shrek is afraid that Donkey is going to be naughty again, so he decides to tie him up so he will not disturb the royal dinner. Shrek grows a circular patch of delicious grass, and decides to rope Donkey to a fence post on its border. However he's afraid that when Donkey gets hungry, he will eat all the grass, and Shrek needs the grass to prepare a dish of tasty ogre grass salad for the dinner. The rope needs to be short, so Donkey won't be able to eat (or, even worse, fertilize) too much grass.

Grass patch

Given the diameter of the circular grass patch (measured in ogre steps), calculate the maximum length of the rope so Donkey won't be able to eat more than given percentage of grass (given as ratio in range 0 <= percentage <= 1, i.e. 0.5 means 50%). As Shrek is just an ogre and is not really familiar with fractions, the length should be returned as whole ogre steps. Beware: in the Fairy Land, grass patches can grow very large!

GeometryPerformance
*/
// Solution
#include <cmath>

double intersection(double R, double L) {
    double d = R;
    if (L >= 2*R) return M_PI*R*R;
    double alpha = acos((d*d + L*L - R*R) / (2*d*L));
    double beta  = acos((d*d + R*R - L*L) / (2*d*R));
    double area =
        L*L*alpha +
        R*R*beta -
        0.5*sqrt((-d+L+R)*(d+L-R)*(d-L+R)*(d+L+R));
    return area;
}

int getRopeLength(int fieldDiameter, double eatenRatio) {
    if (!fieldDiameter || !eatenRatio) return 0;
    if (eatenRatio == 1) return fieldDiameter;
    double R = fieldDiameter / 2.0, total = M_PI * R * R;
    double lo = 0, hi = fieldDiameter;
    for (int i = 0; i < 100; ++i) {
        double mid = (lo + hi) / 2;
        double area = intersection(R, mid);
        if (area / total <= eatenRatio) lo = mid;
        else hi = mid;
    }
    return (int)floor(lo);
}