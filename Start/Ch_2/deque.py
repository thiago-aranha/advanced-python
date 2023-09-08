# deque objects are like double-ended queues
import collections
import string

# TODO: initialize a deque with lowercase letters
d = collections.deque(string.ascii_lowercase)

# TODO: deques support the len() function
print(len(d), "letters")

# TODO: deques can be iterated over
# for letter in d:
#     print(letter.upper())

# TODO: manipulate items from either end
print(d)
print(d.pop())
print(d.popleft())
print(d.append(2))
print(d.appendleft(3))
print(d)

# TODO: use an index to get a particular item
print(d[20])