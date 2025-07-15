def words_in_text(text):
    words = text.split()
    return f"Found {len(words)} total words"

def character_frequency(text):
    text = text.lower()  # Normalize to lowercase
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def sorted_character_frequency(frequency_dict):
    sorted_list = [{"char": char, "num": count} for char, count in frequency_dict.items()]
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list