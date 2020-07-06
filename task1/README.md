# Task 1

Shitty question, shitty wording, everything is shitty about this challenge except for the fact that at last you have to arrange the 3-byte words to form a sentence.

Oh man wtf is `combinations` - read [part1](part1) and you'd find lines like - `he7,vv` - these are `cartesian prodcuts` of characters taken 3 at a time, and not `combinations` :weary:, every byte is 0 to 256 - at max `256**3 = 16777216` values, this would hopefully not cause any memory issues if you're careful with what you write! We can prune the search space to ASCII characters, and even further to only printable characters, because a sensible sentence would probably not involve any non-ASCII(non-printable respectively) characters at all.  

This [script](script.py) reads all the files and then outputs the missing 3-byte long words -
`[' We', ' as', 'All', 'ati', 'ble', 'cre', 'ing', 'is ', 'k f', 'm s', 'olv', 'or ', 'pro', 've ']`

Now we'd like to form the sentence, which is - `All We ask for is creative problem solving` - 42 bytes long or 14 3-byte words. Much irony, nothing creative but sentence forming.

The brownie points script is [here](script2.py). Again simply take the cartesian product thrice, and don't output those 3-byte words which are a part of the sentence. Also do use random.shuffle :) This might cause a lot of trouble if we were to take more than 3 or 4 bytes at a time, since RAM is always limited :/