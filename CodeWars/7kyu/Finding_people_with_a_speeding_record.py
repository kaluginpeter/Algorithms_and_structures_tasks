# Table schematic
# People
# Column	Data Type	Description
# id	int	primary key, the unique identifier
# birthdate	date	the birthdate of a person
# Records
# Column	Data Type	Description
# id	int	primary key, the unique identifier
# person_id	int	the id of the person, who was speeding
# speed_delta	int	by how much the person was too fast (speed - allowed speed)
# record_date	date	the date of the speeding record
# Context
# You are a German police officer. The graphical management system for records about people speeding is currently not online. Since you have some experience with databases you are tasked to manually write a query to find all people and the related records
#
# Task
# Select the id and birthdate of each person. Provide the sum of all speed deltas for each person. Make sure to provide a delta for each person, even if there are no records. In such case return 0 for the total_speed_delta. Your output should be ordered by the person_id in ''ascending order''.
#
# Expected output
# Column	Data Type	Description
# person_id	int	the id of the person, who was speeding
# birthdate	date	the birthdate of a person
# total_speed_delta	int	the sum of all speed deltas
# Hint
# GROUP BY is your friend...
#
# SQLDatabasesFundamentals