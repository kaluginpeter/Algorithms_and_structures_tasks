# As you sit in your university math lecture, your professor introduces the Gauss-Seidel method, an iterative technique for solving systems of linear equations. The method itself was quite elegant, but the idea of manually solving equations repeatedly until convergence was daunting. That's when you decided to take matters into your own hands – or rather, your computer's. You set out to write a program that would automate the Gauss-Seidel method, making those late-night assignment sessions a bit less tedious.
#
# Gauss-Seidel Method
# The Gauss-Seidel method is an iterative technique for solving a system of linear equations. In this kata, your task is to write a function that takes a system of three linear equations in the form of a matrix and return the solution vector with an accuracy of 4 decimal places
#
# The iterative process
# Initialization. Start with an initial guess vector, in this case, a vector of all zeros. (x=y=z=0)
# Iteration. For this method to work (i.e., to converge at a solution), the coefficient matrix should be diagonally dominant. That is, the elements on the leading diagonal of the matrix should dominate the sum of all other coefficients in that row. For the sake of simplicity, the given coefficient will be diagonally dominant. Use the first equation to calculate the value of x, the second to calculate the value of y, and the third to calculate the value of z. For each equation in turn, calculate the updated value for the corresponding variable using the latest values of the other variables. This involves substituting the current values into the corresponding equation and solving for the variable in question.
# Convergence Check After each iteration, compare the current values of the variables to their values from the previous iteration. If the difference between corresponding elements in the vectors is less than 0.0001 for all variables, the solution has converged.
# Repeat If the solution has not converged, repeat steps 2 and 3 until convergence is achieved.
# Example
# Consider the system of equations:
#
# 8x - 3y + 2z = 20
# 4x + 11y - z = 33
# 6x + 3y + 12z = 35
# Here, observe that the the coefficient matrix is diagonally dominant. Use the first equation to obtain a formula for x, the second for a formula of y, and the third for a formula of z.
#
# x = 1/8 * (20 + 3y − 2z)
# y = 1/11 *  (33 − 4x + z)
# z = 1/12 * (35 − 6x − 3y)
# Use 0 as the initial guess for x,y,z. Calculate the values of x,y,z (in that order) using the last updated values for the other two variables.
#
# Iteration 1:
# Calculate x using the last updated values of y and z (both 0), to get x=2.5.
#
# Calculate y using the last updated values of x and z (2.5, 0 respectively), to get y=2.0909.
#
# Calculate z using the last updated values of x and y (2.5, 2.0909 respectively), to get z=1.1439.
#
# Iteration 2:
# Calculate x using the last updated values of y and z (from above), and repeat for y and z.
# Continue repeating this process until succesive updates of the variable are within 0.0001 of each other.
#
# Set the cap for the number of iterations as 100. If the solution has not converged in the first 100 iterations, return the last updated values and the number of iterations in the above format.
#
# Input:
# The input will be in the form of a 3X4 matrix where the first three columns represent the x,y,z values in that order and the last column represents the right side of the equation. The example above is hence represented as, [[8, -3, 2, 20], [4, 11, -1, 33], [6, 3, 12, 35]]
# You can assume that the given system of equations is diagonally dominant and has only one solution.
# Output:
# Return the answer as a two element tuple, where the first element is a list of the x,y,z values in that order, and the second element is the number of iterations conducted. i.e., in the form `([x,y,z],iterations)
# Do not round any of the values of the variables whilst returning.
# AlgorithmsMathematics