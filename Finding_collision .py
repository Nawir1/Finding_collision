##############################################
## Program attempts collision attack on SHA1##
###############################################

import hashlib
import random
import string
def plaintext():
    """Function generates plaintext using random characters"""

    plaintext = ''.join(random.choices(string.ascii_letters, k = 10))

    return plaintext

def sha60v(plaintext):
    """Function generates hash based on SHA-1 and extracts first 60bits"""

    has_h = hashlib.sha1(plaintext.encode()).hexdigest()

    return has_h[:8] ##60 / 4

def find_collision():

    """Function that attempts to find collision"""

    hash_vals = set()
    while True:
        text = plaintext()
        text_hash = sha60v(text)
        if text_hash in hash_vals:
            return text, text_hash
        hash_vals.add(text_hash)

text_return, hash_return = find_collision()
text_return_2 = ''
while sha60v(text_return_2) != hash_return:
    text_return_2 = plaintext()

print(f'Collision Found')
print(f'Message input:: {text_return}')
print(f'Collision text:: {text_return_2}')
print(f'Hash Value:: {hash_return}')

