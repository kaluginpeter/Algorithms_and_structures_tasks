# In the task, you need to calculate whether a Pareto principle is observed for a DVD rentals, which states that 20% of customers will be responsible for approximately 80% of the rentals. You need to write a query that would identify the top 20% of customers based on the number of rentals they had made, and then calculate the percentage of total rentals they accounted for. In the task you need to:
#
# calculate the total number of rentals across all customers.
# identify the top 20% of customers by rentals.
# calculate the number of rentals by these top 20% of customers.
# Finally, to calculate the percentage of rentals by the top 20% of customers compared to the total number of rentals.
# In your query you need to return three pieces of information:
#
# top_20%_rentals_count: The total number of rentals made by the top 20% of customers.
# total_rentals_count: The total number of rentals made by all customers.
# percentage_of_top_20%: The percentage of total rentals made by the top 20% of customers. Should be of numeric type, rounded to 2 decimal places
# Notes:
# for the sample tests, static dump of DVD Rental Sample Database is used, for the final solution - random tests.
# Static dump won't provide belieavable percentage, but random test has been written to correlate with Pareto principle
# What is meant by top 20% of customers? If there are 1000 customers in total, we would first order them by the number of rentals they have made, and then take the top 200 customers in terms of number of rentals. These 200 customers would be considered the "top 20%" of customers.
# What we want to achieve is to cut off exactly 20% of customers regardless of tie. If 20 % is not the whole number - for example, for 599 customers it would be 119.8 - then we need to take upper bound, 120, not 119
# Good luck!
#
# Schema
# (not all columns - only part of the domain required to solve this kata)
#
# rental table:
# Column       | Type      | Modifiers
# -------------+-----------+----------
# rental_id    | integer   | not null
# customer_id  | integer   | not null
# Desired Output
# The desired output should look like this:
#
# top_20%_rentals_count   | total_rentals_count  |     percentage_of_top_20%
# -----------------------+----------------------+--------------------------+
#   7756                 | 10000                |   0.776e2                |
# SQLDatabases
# Solution
WITH customer_rentals AS (
    SELECT
        customer_id,
        COUNT(*) AS rentals_count
    FROM rental
    GROUP BY customer_id
),
customer_stats AS (
    SELECT
        COUNT(*) AS customers_count,
        SUM(rentals_count) AS total_rentals_count
    FROM customer_rentals
),
top_customers AS (
    SELECT rentals_count
    FROM customer_rentals
    ORDER BY rentals_count DESC
    LIMIT (
        SELECT CEIL(customers_count * 0.2)::int
        FROM customer_stats
    )
)
SELECT
    SUM(rentals_count)::int AS "top_20%_rentals_count",
    cs.total_rentals_count::int AS "total_rentals_count",
    ROUND(
        100.0 * SUM(rentals_count) / cs.total_rentals_count,
        2
    ) AS "percentage_of_top_20%"
FROM top_customers
CROSS JOIN customer_stats cs
GROUP BY cs.total_rentals_count;