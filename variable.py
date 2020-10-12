# this is the first comment
the_word_is_flat = True # and this is the second comment
                        # .. comment
if the_word_is_flat:
    print('Be careful not fall off!')

2 + 2

50 -5*6

# Lists
squares = [1, 4, 9, 16, 25]
squares[0]

#Fibonacci series
## the sum of two element defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b

# String
# formatting with the .format() method
# a good way to format object into your strings print statements is with the string .format() method. the syntax 
# 'String here{} then also{}'.format('something1', 'something2')

print("this's a string {}".format("inserted"))   
print("The {} {} {}".format('fox', 'brown', 'quick'))   
# print "The fox brown quick"

result = 100/777
print("The result was {r:1.3f}".format(r=result))
# r: 3f before not get 3 characters. default: 0.1287001287001287
