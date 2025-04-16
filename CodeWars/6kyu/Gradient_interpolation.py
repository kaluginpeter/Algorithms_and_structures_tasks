# You're involved in the creation of a game. In this game, a certain function is to be used to generate colors dynamically, such that, say, different temperatures will produce different colors. This function can be replaced during the gameplay, or even chosen by the player. The exact choices aren't finalized, but you know that a simple linear gradient will be used.
#
# Your task is to implement a higher-order function that takes two colors in RGB format, and returns another function representing a linear gradient which interpolates between them using an integer (lying in range [0; 100]) provided as an input and returns this interpolated color. The resulting RGB components must be rounded down.
#
# Fundamentals