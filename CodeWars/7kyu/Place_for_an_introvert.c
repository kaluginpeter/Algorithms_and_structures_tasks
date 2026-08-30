/*
Place for an Introvert
Scenario
Imagine you are an extreme introvert. You need to find a place to sit in a public area (like a bus, cinema, or lecture hall). The most important condition for your psychological comfort is choose a suitable location with no active or potential neighbors on either side.

But introverts are clever: they think one step ahead. You need to write an algorithm that chooses a seat that minimizes the number of current neighbors and limits the chance of someone sitting right next to you in the future.

Tactical Seating Rules
The input is a string seats consisting of the following characters:

0 — an empty seat;
1 — an occupied seat;
  (space) — an aisle, gap, or wall (a safe zone; people across a space do not disturb you).
Each empty seat (0) is evaluated by the number of threats to its left and right sides. A side is considered a threat if it contains:

An occupied seat (1) — a current neighbor.
An empty seat (0) — a potential future neighbor who might sit there later.
The boundaries of the string and spaces ( ) are not threats (nobody can sit there).

Critical Rule: An introvert will never accept a seat with 2 threats (trapped between current or potential neighbors on both sides). If a seat has 2 threats, it is considered completely unacceptable.

The introvert always chooses the seat with the minimum total number of threats, as long as it has fewer than 2 threats.

Note: If multiple valid seats have the exact same minimum number of threats (0 or 1), the introvert will always choose the first available option from left to right.

Output
The function should return a string representing the seating arrangement, with the chosen ideal empty seat marked as occupied (1).
If there are no empty seats (0) available, or if all available seats are unacceptable (have 2 threats), the function must return None / nil.
Examples
"1000100" -> "1000101"
"000" -> "100"
"000 01" -> "100 01"
"101" -> None / nil
"10101" -> None / nil
StringsArrays
*/