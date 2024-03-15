# Print all integers from 0 to 150
print("Basic:")
for i in range(151):
    print(i, end=' ')
print("\n")

#  Print all the multiples of 5 from 5 to 1,000
print("Multiples of Five:")
for i in range(5, 1001, 5):
    print(i, end=' ')
print("\n")

# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo"
print("Counting, the Dojo Way:")
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo", end=' ')
    elif i % 5 == 0:
        print("Coding", end=' ')
    else:
        print(i, end=' ')
print("\n")

#  Add odd integers from 0 to 500,000, and print the final sum.
print("Whoa. That Sucker's Huge:")
sum_of_odds = 0
for i in range(1, 500001, 2):
    sum_of_odds += i
print("Sum of odd integers from 0 to 500,000:", sum_of_odds, "\n")

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours
print("Countdown by Fours:")
for i in range(2018, 0, -4):
    print(i, end=' ')
print("\n")

#Set three variables: lowNum, highNum, mult. Start at lowNum and going through highNum, print only the integers that are a multiple of mult
lowNum = 2
highNum = 9
mult = 3
print("Flexible Counter:")
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i, end=' ')
print("\n")
