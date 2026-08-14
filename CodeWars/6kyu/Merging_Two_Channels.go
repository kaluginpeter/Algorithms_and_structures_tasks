/*
Introduction
Go has a powerful built-in data type: channel. In some cases you want process messages from different data sources (e.g. UDP packages, TCP messages, HTTP requests) and you want to consume all in the same way. Then it might make sense to merge multiple channels into a single one. This is what we do here.

PS: Once you solved this kata, there is an advanced version waiting for you: Merging N Channels :)

Learning Goal
In this kata we learn to merge two channels into a single one by utilizing concurrency patterns.

Task
Write a function func Merge(a <-chan string, b <-chan string) <-chan string, which takes two read-only channels and returns a new channel. All messages from channel a and b must be forwarded to the new channel. Once a and b are both closed, also the returned channel must be closed.

The order of the forwarded messages doesn't matter, but you should consume from both incoming channels concurrenly.

Example
// channel a contains 3 messages
a := make(chan string, 3)
a<-"foo"
a<-"bar"
a<-"baz"
close(a)

// channel b contains 2 messages
b := make(chan string, 2)
b<-"hello"
b<-"world"
close(b)

// your implementation
c := Merge(a, b)

// when messages are consumed from c, it must return all 5 messages from a and b,
// while the order of the messages is not defined
<-c // "foo"
<-c // "bar"
<-c // "hello"
<-c // "world"
<-c // "baz"

// channel c must be closed at this point
Concurrency
*/