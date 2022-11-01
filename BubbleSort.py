"""
Try implementing bubble sort algorithm.
Sort numbers from lowest to highest for example.

It functions in following way:
There is a list of random numbers.
It will take first number on list and compare it to the adjecant one(next one) 
If condition is satisfied it moves on.
In case of sorting numbers from lowest to highest, it will put lower numbers on left, higher on right.
But it will have to go in multiple passes to truly sort it.

list: 3 4 2 1 5
first pass:
is 3 < 4 ? yes - pass
is 4 < 2 ? no - swap
is 1 < 5 ? yes - pass

second pass: 3 2 4 1 5
is 3 < 2 ? no - swap
is 3 < 4 ? yes - pass
is 4 < 1 ? no - swap
is 4 < 5 ? yes - pass -> apparently this would not happen or would, needs more investigation because highest numbers are usually at right and it's remembered

third pass: 2 3 1 4 5
is 2 < 3 ? yes - pass
is 3 < 1 ? no - swap
is 3 < 4 ? yes - pass ** at this point 4 and 5 wouldn't be compared because of last time maybe? on first pass 4 and 5 were never compared

fourth pass: 2 1 3 4 5
is 2 < 1 ? no - swap
is 2 < 3 ? yes - pass ** would this check occur or not because 2 and 3 were compared in past, inefficient but probably it wouldn't even occur and program would stop
"""