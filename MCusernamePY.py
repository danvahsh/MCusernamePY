from english_words import english_words_lower_alpha_set
from better_profanity import profanity
from mojang import API

mojangapi = API()

for word in english_words_lower_alpha_set:
    flagged = profanity.contains_profanity(word)
    if flagged == False:
        uuid = mojangapi.get_uuid(word)
        if not uuid:
            print("\n", word, "is probably not taken", "\n")
            with open("avaliable_usernames.txt", "a") as list:
                current_word = word + "\n"
                list.write(current_word)
