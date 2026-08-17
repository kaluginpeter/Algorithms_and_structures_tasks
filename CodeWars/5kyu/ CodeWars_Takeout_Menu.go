

/*
CodeWars Takeout Menu
Appetizers / Sushi
Food Menu
Note: There is a preloaded function GetMenu() that will return a map[string]float32 containing the full menu + pricing that may be used.
Task
Your task at the CodeWars restaurant is to answer phone calls and take customer orders, telling them the final cost at the end of each phone call. The catch with this kata though is that it useschannels to communicate with your Solution rather than the typical single function call and return.

Details
Customer Dialogue:
The customer will always open the conversation with place an order
The customer may ask for a price {item}
The customer confirms they want an item by saying order {item}
The customer may ask for an item that is not on the menu
The order ends when the customer says that is all
Expected Responses:
Respond with ok for
place an order
order {item} - (unavailable if not on the menu)
Respond with the price as a string for
price {item} - (unavailable if not on the menu)
that is all
Respond to goodbye with goodbye
When to stop
You should continue to take orders until you receive on the done channel. You can assume that you will not receive on the done channel while you are also receiving on hear, it is one or the other. You can also assume that you won't receive on done in the middle of an order.

Example Phone Call
Each newline is a receive on the hear channel, tabbed in lines are responses

place an order
    ok
price chicken bento box
    12.99
price spring roll
    1.99
order spring roll
    ok
order spring roll
    ok
order chicken bento box
    ok
price pizza
    unavailable
that is all
    16.97
goodbye
    goodbye
Fundamentals
*/