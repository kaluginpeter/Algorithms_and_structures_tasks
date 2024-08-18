# Given the molecular mass of two molecules
# �
# 1
# M
# 1
# ​
#   and
# �
# 2
# M
# 2
# ​
#  , their masses present
# �
# 1
# m
# 1
# ​
#   and
# �
# 2
# m
# 2
# ​
#   in a vessel of volume
# �
# V at a specific temperature
# �
# T, find the total pressure
# �
# �
# �
# �
# �
# �
# P
# total
# ​
#   exerted by the molecules. Formula to calculate the pressure is:
#
# �
# �
# �
# �
# �
# �
# =
# (
# �
# 1
# �
# 1
# +
# �
# 2
# �
# 2
# )
# �
# �
# �
# P
# total
# ​
#  =
# V
# (
# M
# 1
# ​
#
# m
# 1
# ​
#
# ​
#  +
# M
# 2
# ​
#
# m
# 2
# ​
#
# ​
#  )RT
# ​
#
# Input
# Six values :
#
# �
# 1
# M
# 1
# ​
#  ,
# �
# 2
# M
# 2
# ​
#  : molar masses of both gases, in
#
# �
# ⋅
# �
# �
# �
# −
# 1
#  g⋅mol
# −1
#
# �
# 1
# m
# 1
# ​
#   and
# �
# 2
# m
# 2
# ​
#  : present mass of both gases, in grams (
# �
# g)
# �
# V: volume of the vessel, in
#
# �
# �
# 3
#  dm
# 3
#
# �
# T: temperature, in
#
# °
# �
#  °C
# Output
# One value:
# �
# �
# �
# �
# �
# �
# P
# total
# ​
#  , in units of
# �
# �
# �
# atm.
#
# Notes
# Remember: Temperature is given in Celsius while SI unit is Kelvin (
# �
# K).
#
# 0
# °
# �
# =
# 273.15
# �
#  0°C=273.15K
#
# The gas constant
#
# �
# =
# 0.082
# �
# �
# 3
# ⋅
# �
# �
# �
# ⋅
# �
# −
# 1
# ⋅
# �
# �
# �
# −
# 1
#  R=0.082dm
# 3
#  ⋅atm⋅K
# −1
#  ⋅mol
# −1
#
#
# FUNDAMENTALS
# Solution
def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    n1 = given_mass1 / molar_mass1
    n2 = given_mass2 / molar_mass2
    R = 0.082
    temp += 273.15
    p1 = n1 * R * temp / volume
    p2 = n2 * R * temp / volume
    return p1 + p2