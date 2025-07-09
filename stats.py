def count_words_in_text(text):
    return len(text.split())

def count_used_characters(text):
    characters = {}
    for character in text.lower():
        if (character not in characters):
            characters[character] = 1
        else:
            characters[character] += 1

    return characters

def sort_on(items):
    return items["num"]

def sort_chars(dictionary):
    sorted_chars = []
    for character in dictionary:
        character = {"char": character, "num": dictionary[character]}
        sorted_chars.append(character)
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars