/*
Introduction
Snakes and Ladders is an ancient Indian board game regarded today as a worldwide classic. It is played by two or more players on a game board with numbered, gridded squares. A number of "ladders" and "snakes" are pictured on the board, each connecting two specific squares. (Source: Wikipedia)


Task
Your task is to create a simple class called SnakesLadders. The test cases will call the method play(die1, die2) independently of the state of the game or the player turn. The arguments die1 and die2 are the dice thrown in a turn and are both integers between 1 and 6. The player will make a number of steps equal to the sum of die1 and die2, moving one square per step.

The Board

Rules
There are two players, and both start off the board on square 0.
Player 1 starts and alternates with player 2.
You follow the numbers up the board in order from 1 to 100.
If the values of both dice are the same, that player will have another turn after the current turn ends.
Climb up ladders. The ladders on the game board allow you to move upwards and get ahead faster. If you land exactly on a square that shows the bottom of a ladder, you may move the player all the way up to the square at the top of the ladder (even if you roll a double).
Slide down snakes. Snakes move you back on the board. If you land exactly on the top of a snake, you must slide all the way down to the square at the bottom of the snake or chute (even if you roll a double).
Land exactly on the last square to win. The first player to reach the highest square on the board wins. If you roll too high, your player "bounces" off square 100 and continues moving backward for the remaining steps. You can only win by rolling the exact number needed to land on the last square. For example, if you are on square 98 and roll a five, move your piece to 100 (two steps), then "bounce" back to 99, 98, and 97 (three, four, then five steps).
If the player rolls a double and lands on the finish square (100) after taking all steps for the roll, the player wins the game and does not take another turn.
Returns
Return "Player n Wins!" where n is the winning player who has landed on square 100 after taking all steps in their turn.

Return "Game over!" if a move is attempted after any player has won.

Otherwise, return "Player n is on square x", where n is the current player and x is the square they are currently on.

Good luck and enjoy!

Kata Series
If you enjoyed this, then please try one of my other Katas. Any feedback, translations and grading of beta Katas are greatly appreciated. Thank you.

Rank
Maze Runner
Rank
Scooby Doo Puzzle
Rank
Driving License
Rank
Connect 4
Rank
Vending Machine
Rank
Snakes and Ladders
Rank
Mastermind
Rank
Guess Who?
Rank
Am I safe to drive?
Rank
Mexican Wave
Rank
Pigs in a Pen
Rank
Hungry Hippos
Rank
Plenty of Fish in the Pond
Rank
Fruit Machine
Rank
Car Park Escape
Design PatternsGamesFundamentals
*/
// Solution
#include <bits/stdc++.h>
using namespace std;

class SnakesLadders {
private:
    vector<int> pos;
    int current;
    bool gameOver;
    unordered_map<int, int> jumps;

public:
    SnakesLadders() {
        pos = {0, 0};
        current = 0;
        gameOver = false;

        jumps = {
            {2,38}, {7,14}, {8,31}, {15,26}, {21,42}, {28,84}, {36,44}, {51,67}, {71,91}, {78,98}, {87,94},
            {16,6}, {46,25}, {49,11}, {62,19}, {64,60}, {74,53}, {89,68}, {92,88}, {95,75}, {99,80}
        };
    }

    string play(int die1, int die2) {
        if (gameOver) return "Game over!";
        int move = die1 + die2;
        int &p = pos[current];
        p += move;
        if (p > 100) p = 100 - (p - 100);
        if (jumps.count(p)) p = jumps[p];
        if (p == 100) {
            gameOver = true;
            return "Player " + to_string(current + 1) + " Wins!";
        }
        string result = "Player " + to_string(current + 1) + " is on square " + to_string(p);
        if (die1 != die2) current ^= 1;
        return result;
    }
};