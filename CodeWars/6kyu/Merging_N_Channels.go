/*
Introduction
This kata is an advanced version of Merging Two Channels. It's recommended to solve that one first, as it already solves half of this problem :)

Go has a powerful built-in data type: channel. In some cases you want process messages from different data sources (e.g. UDP packages, TCP messages, HTTP requests) and you want to consume all in the same way. Then it might make sense to merge multiple channels into a single one. This is what we do here.

Learning Goal
In this kata we learn to merge any amount of channels into a single one by utilizing concurrency patterns.

Task
Write a function func Merge(c ...chan string) <-chan string, which takes any amount of channels and returns a new channel. All messages from the input channels must be forwarded to the new channel. Once all input channels are closed, also the returned channel must be closed.

The order of the forwarded messages doesn't matter, but you should consume from all incoming channels concurrenly.

Example
Merging Two Channels
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
merged := Merge(a, b)

// when messages are consumed from the merged channel, it must return all 5 messages from a and b, while the order of the messages is not defined
// afterwards the merged channel must be closed
Merging Four Channels
// channel a contains 3 messages
a := make(chan string, 3)
a<-"a-foo"
a<-"a-bar"
a<-"a-baz"
close(a)

// channel b contains 2 messages
b := make(chan string, 2)
b<-"b-foo"
b<-"b-bar"
close(b)

// channel c contains 2 messages
c := make(chan string, 2)
c<-"c-foo"
c<-"c-bar"
close(c)

// channel d contains 3 messages
d := make(chan string, 3)
d<-"d-foo"
d<-"d-bar"
d<-"d-baz"
close(d)

// your implementation
merged := Merge(a, b, c, d)

// when messages are consumed from the merged channel, it must return all 10 messages from a, b, c and d, while the order of the messages is not defined
// afterwards the combined channel must be closed
ConcurrencyLanguage Features
*/
// Solution
package kata

import "sync"

func Merge(c ...chan string) <-chan string {
	out := make(chan string)

	var wg sync.WaitGroup
	wg.Add(len(c))

	for _, ch := range c {
		go func(ch chan string) {
			defer wg.Done()
			for msg := range ch {
				out <- msg
			}
		}(ch)
	}

	go func() {
		wg.Wait()
		close(out)
	}()

	return out
}