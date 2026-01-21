import random
import string



def generate_short_url():
    link = random.sample(random.choice([string.ascii_letters for _ in range(10)]) ,k=5)
    word = "".join(link)

    return word
