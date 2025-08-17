def words_count(text):
    words = text.split()
    return len(words)

def characters_count(text):
    char_count = {}
    for word in text.split():
        for char in word:
            char = char.lower()
            char_count[char] = char_count.get(char, 0) + 1
        #char_count[" "] = char_count.get(" ", -1) + 1
    return char_count

def sort_on(items):
    return items["count"]

def sort_characters_count(char_count):
    sorted_list_char_count = []
    for key, value in char_count.items():
        sorted_list_char_count.append({"char": key, "count": value})
    sorted_list_char_count.sort(key=sort_on, reverse=True)
    return sorted_list_char_count