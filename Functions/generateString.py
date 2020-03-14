import random
import string


def generateString(length=10):
    generate_letter = string.ascii_letters
    generate_link = "".join(random.choice(generate_letter) for _ in range(length))
    return generate_link


# sample = generateString()
# print(sample)