# Task 3

We're given an IP address, where we can enter a username and it would tell if the username exists or not. Well, we're also given the source code.

The next thing pretty obvious in the source code is that we have SQLi vulnerability in the username field, since it simply concatenates the username field to the query -  
`$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";`

If the query returns atleast one result, assuming `username` is unique, the output is `This user exists`, else if the query doesn't return anything, the output is `This user doesn't exist`. Trying out all possible combinations of ASCII letters doesn't seem feasible, we'd have to search another way.  
Trying rockyou would also be a good idea, but the best thing is to use incremental attack :wink:.  
Oh what's an incremental attack? We'd try all possible characters at a position, and if the character matches the character of the password at that position, we'd move on to the next position, until we find a position at which no character matches, implying that the string before trying the match is our password. Why would this work? Well, because, we can do prefix queries in MySQL - `SELECT * from users where username="admin" and password LIKE "abc%"` - would give all the users whose username is admin and password begins with "abc"! Cool! This is like padding oracle attack of some sort(imo) - if the prefix matches, you're going the right way, else try other characters.

The [script](script.py) does the job, and it tells us the password - `cp6xycx9r42y3q5jsvl8mthwwc8zuccj`.

We can check if this is indeed the correct password - `SELECT * from users where username="admin" and password="cp6xycx9r42y3q5jsvl8mthwwc8zuccj"` - to execute this query - enter in the username field on the site - `admin" and password="cp6xycx9r42y3q5jsvl8mthwwc8zuccj` and we get back `This user exists` :happy: