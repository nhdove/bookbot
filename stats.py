def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    counts = {}
    for char in text:
        char = char.lower()
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_character_key(item):
    return item["num"]

def sorted_character_count(counts):
    count_items = []
    for char, count in counts.items():
        count_items.append({
            "char": char,
            "num": count
        })
    count_items.sort(key=sort_character_key, reverse=True)
    return count_items
