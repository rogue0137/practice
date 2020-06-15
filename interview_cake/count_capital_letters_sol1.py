# Write a one-liner that will count the number of capital
#  letters in a file. Your code should work even if the
# file is too big to fit in memory.

fh = 'What is your name? Is it Fred?'

count = sum(character.isupper() for line in fh for character in line)
# """
# Sum results from below.
#
# For line in fh:
#     For character in line:
#         if character.isupper(), then true (1)
# """

print(count)
