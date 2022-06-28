#Generator Excercises

#Problem 1
#Create a generator, primes_gen that generates prime numbers starting from 2.
def primes_gen():
    n=1
    while True:
        n+=1
        for number in range(2,n+1):
            if n== number:
                yield n
            if n % number==0:
                break


gen = primes_gen()
for _ in range(10):
    print(next(gen), end=' ')
# Expected output
# 2 3 5 7 11 13 17 19 23 29
#----------------------------------------------------------------------------

#Problem 2
#Create a generator, unique_letters that generates unique letters from
#the input string. It should generate the letters in the same order as
#from the input string.
def unique_letters(str):
    unique_letters=""
    for char in str:
        if char not in unique_letters:
            unique_letters+=char
        yield unique_letters
for letter in unique_letters('hello'):
    print(letter, end=' ')
# Expected output
# h e l o