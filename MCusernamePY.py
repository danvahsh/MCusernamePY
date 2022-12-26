from english_words import english_words_lower_alpha_set
from mojang import MojangAPI

for word in english_words_lower_alpha_set:
    uuid = MojangAPI.get_uuid(word)
    if not uuid:
        print("\n", word, "is not taken", "\n")
        list = open("avaliable.usernames", "a")
        current_word = word + "\n"
        list.write(current_word)
        list.close()
