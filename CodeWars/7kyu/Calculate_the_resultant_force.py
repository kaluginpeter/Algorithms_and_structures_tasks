# Given two forces (F1 and F2 ) and the angle F2 makes with F1 find the resultant force R and the angle it makes with F1.
#
# input
# Three values :
#
# F1
# F2 making an angle θ with F1
# angle θ
# output
# An array consisting of two values :
#
# R (the resultant force)
# angle R makes with F1 (φ)
# notes
# Units for each of the following are given as under :
#
# F1 = Newton
# F2 = Newton
# angle θ = degree
# R = Newton
# φ = degree
# PhysicsGeometryAlgorithms
# Solution
import math

def solution(F1, F2, theta):
    theta_rad = math.radians(theta)
    F1_x = F1
    F1_y = 0
    F2_x = F2 * math.cos(theta_rad)
    F2_y = F2 * math.sin(theta_rad)
    R_x = F1_x + F2_x
    R_y = F1_y + F2_y
    R = math.sqrt(R_x**2 + R_y**2)
    phi = math.degrees(math.atan2(R_y, R_x))
    return [R, phi]