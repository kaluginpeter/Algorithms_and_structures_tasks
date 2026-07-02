# A tire size is written in the format "205/55R16" where:
#
# 205 → tire width in millimeters
# 55 → aspect ratio (sidewall height as a percentage of width)
# 16 → rim diameter in inches
# The construction code between aspect ratio and rim diameter can be R, ZR, B, or D.tire-dimensions-by-code-gs-night-landscape-750.webpGiven a tire size string and a distance in kilometers, return the number of rotations the tire makes.
#
# Function signature:
#
# def tire_rotations(tire_size: str, distance_km: float) -> float:
# Examples:
#
# tire_rotations("205/55R16", 110) ≈ 55410.8047
# tire_rotations("185/65ZR15", 900) ≈ 460947.5423
# tire_rotations("225/45B17", 0) == 0.0
# Notes:
#
# Use π = math.pi
# 1 inch = 25.4 mm
# Regular ExpressionsMathematicsParsingFundamentals