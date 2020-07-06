# Task 2

Really saxy and cool task! Oh well CTFs are always guessy :)

Oh my brain has been literally stormed by this task! Didn't expect this brilliant-ness! We're given this [output.txt](output.txt) but have no idea where the fkin equations are located at! Tried [CyberChef Magic](https://gchq.github.io/CyberChef/) but to no benefits, then tried something else like binary indexing of Base64 and shit, but again no ups!  

Oh well I couldn't see the hidden representation because I had word-wrapping toggled ON in my IDE XD! On turning it off, suddenly something familiar seems coming to you, calculator font :)(couldn't come up with a better name, my bad) Every digit, as well as brackets and operators are written in 7 lines, with 1 representing say black and 0 representing say white.  
One could as well take every 7 lines, and convert them to image format, and read the image to easily realise that it's calculator font. Note that every two consecutive characters are separated by column(s) of zeros.  
So all we have to do is recognise the characters - whether it's a digit, or a bracket or an operator - and then form equations from them, which we can evaluate later on.  
ML? No ML needed :stuck_out_tongue:! We can literally hard-code every character with what it represents, and then we can use `eval` very simply!  

In [this](vals.txt) file, I have hardcoded the characters, and in the [script](script.py), I have hardcoded what they represent respectively. Executing the script, we get the huge output, which has been put in [op.txt](op.txt) file!
