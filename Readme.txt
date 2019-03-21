Question A:

python QuestionA.py x1 x2 x3 x4

Input : x1 => integer
        x2 => integer
        x3 => integer
        x4 => integer

Test cases : 

(0, 2) (1, 3) => true
(0, 1) (2, 3) => false
(4, 1) (3, 2) => true
(0, 0) (0, 0) => true
(0, 1) (1, 2) => false
(-4, -2) (-3, -1) => true

I'm assuming that when the end of line 1 and the start of line 2 
it doesn't count as intersecting. 
If the lines are just points (0, 0) and are on the exact same point,
it counts as intersecting.

I'm also assuming that inputs are valid. (QuestionA.py x1 x2 x3 x4)
All Xs must be integers

Output: True (The lines intersect) False (The lines don't intersect)

--------------------------------------------------------------------------

Question B:

python QuestionB.py versionA versionB

Input: versionA => string (alphanum separated by '.')
       versionB => string (alphanum separated by '.')
       
Test cases:

1.2 1.2 => 1.2 is equal to 1.2
2.0 1.0 => 2.0 is greater than 1.0
1.0 2.0 => 1.0 is less than 2.0
1.2.3.4 1.2.3 => 1.2.3.4 is greater than 1.2.3
1.2.1a 1.2.1b => 1.2.1a is less than 1.2.1b
a.b a.b.c => a.b is less than a.b.c

I'm assuming the inputs are valid

--------------------------------------------------------------------------

Question C:

For question C, I could only complete points 1 and 7.

python QuestionC.py cache_size expiry_time

Input: cache_size => Integer
	   expiry_time => Integer (seconds)

This script works with a while True loop. At launch the cache is empty, enter a value to reference it and
put it in the cache. Every time a new value is referenced, the cache is printed, so we see the current state.
To end type "quit". To test the expiry, you can either keep adding values while keeping the expiry time in mind,
or type "expiry", which will wait for the expiry time + 1 second and then add the value "test_value", which will
then be the only value in the cache.
	   