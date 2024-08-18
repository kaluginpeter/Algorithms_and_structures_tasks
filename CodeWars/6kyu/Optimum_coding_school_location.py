# Preface
# You are currently working together with a local community to build a school teaching children how to code. First plans have been made and the community wants to decide on the best location for the coding school. In order to make this decision data about the location of students and potential locations is collected.
#
# Problem
# In order to be able to attract and teach as many students as possible we want to minimize the total traveling distance for potential students. The streets system is organized in a traditional grid system and students can only travel horizontally or vertically (not diagonal).
#
# The locations of interested students is given as an array with the first value of each entry presenting the x coordinate and the second value presenting the y coordinate:
#
# students = [[3,7],[2,2],[14,1], ...];
# Potential locations are passed as an array of objects with an unique id, a x and y coordinate:
#
# locations = [{"id": 1, "x": 3, "y": 4}, {"id": 2, "x": 8, "y": 2}, ...];
# Your task is now to evaluate which of the school locations would be best to minimize the distance for all potential students to the school.
#
# The desired output should consist of a string indicating the ID of the best suitable location and the x and y coordinates in the following form:
#
# "The best location is number 1 with the coordinates x = 3 and y = 4"
# ALGORITHMS
# Solution
def optimum_location(students, locations):
    total, total_value = float('inf'), None
    for start in locations:
        top: int = 0
        for stud in students:
            top += abs(stud[0] - start['x']) + abs(stud[1] - start['y'])
        if top < total:
            total, total_value = top, start
    return f'The best location is number {total_value["id"]} with the coordinates x = {total_value["x"]} and y = {total_value["y"]}'