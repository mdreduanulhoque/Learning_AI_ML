"""
Evaluate and print the result of the following expression:

x = 10 + 3 * 2 ** 2

Based on what you learnt in the lecture explain why the output is what it is.
"""

"""
Ans:
According to the order precedence, (2 ** 2) will execute first.
It wil become: x = 10 + 3 * 4

Then (3 * 4) will be executed.
It will become: x = 10 + 12

And, lastly (10 + 12) will be executed.
THe final expression will be: x = 22
"""