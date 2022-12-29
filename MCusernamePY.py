from english_words import english_words_lower_alpha_set
from better_profanity import profanity
from mojang import API
import time

program_version = '0.1'

print(f'''MCusernamePY [Version {program_version}] | (c) 2022-Present Daniel Vahsholtz''')

mojangapi = API()

for word in english_words_lower_alpha_set:
    flagged = profanity.contains_profanity(word)
    if flagged == False:
        uuid = mojangapi.get_uuid(word)
        time.sleep(0.33333333333)
        if not uuid:
            print("\n", word, "is probably not taken", "\n")
            with open("avaliable_usernames.txt", "a") as list:
                current_word = word + "\n"
                list.write(current_word)
