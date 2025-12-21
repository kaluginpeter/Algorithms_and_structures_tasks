/*
You are given a node that is the beginning of a linked list. This list contains a dangling piece and a loop. Your objective is to determine the length of the loop.

For example in the following picture the size of the dangling piece is 3 and the loop size is 12:



// Use the `getNext()` method to get the following node.
nodePtr->getNext()
Notes:

do NOT mutate the nodes!
in some cases there can be just a loop, with no dangling piece.
Don't miss dmitry's article in the discussion after you pass the Kata !!

AlgorithmsLinked ListsPerformance
*/
// Solution
int getLoopSize(Node* startNode)
{
    Node* slow = startNode;
    Node* fast = startNode->getNext();
    while (slow != fast) {
        slow = slow->getNext();
        fast = fast->getNext()->getNext();
    }
    int output = 1;
    fast = fast->getNext();
    while (slow != fast) {
        ++output;
        fast = fast->getNext();
    }
    return output;
}