# Task 1

Shitty question, shitty wording, everything is shitty about this challenge except for the fact that at last you have to arrange the 3-byte words to form a sentence.

Oh man wtf is `combinations` - read [part1](part1) and you'd find lines like - `he7,vv` - these are cartesian prodcuts of ASCII characters, every byte is 0 to 127(just a guess) - at max `127**3 = 2097152` values, this would not cause any memory issues at all!  

This [script](script.py) reads all the files and then outputs the missing 3-byte long words.
`[' We', ' as', 'All', 'ati', 'ble', 'cre', 'ing', 'is ', 'k f', 'm s', 'olv', 'or ', 'pro', 've ']`

Now we'd like to form the sentence, which is - `All We ask for is creative problem solving` - 42 bytes long or 14 3-byte words. Much irony, nothing creative but sentence forming.

The brownie points script is [here](script2.py). Again simply take the cartesian product thrice, and don't output those 3-byte words which are a part of the sentence. Also do use random.shuffle :)