
def parse_key_value_string(input_string):
    result = {}
    pairs = input_string.split()
    for pair in pairs:
        if "=" in pair:
            key, value = pair.split('=')
            value = value.strip('"')
            result[key] = value
        else: 
            key = "meta"
            result[key] = pair
    
    return result

def find_word_before_string(input_string, target_string):
    index = input_string.rfind(target_string)
    if index != -1:
        i = index - 1
        while i >= 0 and not input_string[i].isspace():
            i -= 1
        word_before = input_string[i + 1:index].strip()
        if word_before:
            return word_before
    return None


def extract_dollar_strings(input_string):
    words = input_string.split()
    dollar_strings = []
    for word in words:
        if word.startswith('$'):
            dollar_strings.append(word)
    
    return dollar_strings


