###Exercise 62: Roulette Payouts

A roulette wheel has 38 spaces on it. Of these spaces, 18 are black, 18 are red, and two
are green. The green spaces are numbered 0 and 00. The red spaces are numbered 1,
3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 and 36. The remaining integers
between 1 and 36 are used to number the black spaces.
Many different bets can be placed in roulette. We will only consider the following
subset of them in this exercise:
• Single number (1 to 36, 0, or 00)
• Red versus Black
• Odd versus Even (Note that 0 and 00 do not pay out for even)
• 1 to 18 versus 19 to 36
Write a program that simulates a spin of a roulette wheel by using Python’s
random number generator. Display the number that was selected and all of the bets
that must be payed. For example, if 13 is selected then your program should display:
42 2 Decision Making
The spin resulted in 13...
Pay 13
Pay Black
Pay Odd
Pay 1 to 18
If the simulation results in 0 or 00 then your program should display Pay 0
or Pay 00 without any further output.

