
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



#############

def first_non_alpha_offset(line):
    for idx in range(0, len(line)):
        if line[idx] == '$':
            continue

        if not line[idx].isalnum():
            return idx

    return len(line)


def cut_from_to(line, frm, to):
    a_idx = line.index(frm) + len(frm)
    line_rest = line[a_idx:]
    b_idx = line_rest.index(to)

    return line[a_idx:b_idx+a_idx]

    #for idx in range(0, len(line)):
    #    if line[idx] == '$':
    #        continue
#
 #       if not line[idx].isalnum():
  #          return idx

        
