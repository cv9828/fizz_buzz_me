#!/usr/bin/env python

def fizz_buzz(number):
    """Return a string representing the number, or 'fizz'/'buzz'/'fizzbuzz'"""
    # TODO - remove 'pass' and write teh codes
   # for n in range (1,20):
    if number%3==0 and number%5==0:
        return "fizzbuzz"
    elif number%5==0:
        return "buzz"
    elif number%3==0:
        return "fizz"
    else:
        return str(number)

def main():
    """Print sample output of fizz_buzz function"""
    NUMBER = 20
    print("Sample fizz_buzz output for 1 to {0}:".format(NUMBER))
    for i in range(1, NUMBER):
        print(fizz_buzz(i))


##########################

if __name__ == '__main__':
    main()
