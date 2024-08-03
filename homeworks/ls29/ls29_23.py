def word_count(text):
    return len(text.split())

def character_count(text):
    return len(text)

def find_word(text, word):
    ls = text.split()
    if word in ls:
        return True
    return False

def replace_word(text, old_word, new_word):
    ls = text.split()
    old_word = new_word
    return text


dict_operation = {
    'word_count': word_count,
    'character_count': character_count,
    'find_word': find_word,
    'replace_word': replace_word
}

def process_text(text, operation, **kwargs):
    if operation in dict_operation:
        return dict_operation[operation](text, **kwargs)

# Example usage
text = "Hello world! This is a test text. Hello again."

print(process_text(text, 'word_count'))
print(process_text(text, 'character_count'))
print(process_text(text, 'find_word', word='Hello'))
print(process_text(text, 'replace_word', old_word='Hello', new_word='Hi'))