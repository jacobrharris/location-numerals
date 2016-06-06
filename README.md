# Location Numerals - Python Implementation

Your mission, should you choose to accept it, is to create a class in whatever programming language you’re most comfortable with to convert from decimal numbers to location numerals and back. This class should have 3 methods:

* One method that takes an integer and returns the location numeral in abbreviated form. That is, you pass in 9 and it returns “ad"
* One method that takes a location numeral and returns its value as an integer. That is, you pass “ad” in, and it returns 9
* One method that takes a location numeral and returns it in abbreviated form. That is, you pass in “abbc” and it returns “ad"

This method should handle numbers up to 2^26 (67108864). Bonus points if you aren’t restricted by this limit. Please refer to the wikipedia article linked below for an explanation and overview of how location numerals work: http://en.wikipedia.org/wiki/Location_arithmetic#Location_numerals

# Run
`python location_numerals.py -1 87 -2 'ad' -3 'abbc'`
