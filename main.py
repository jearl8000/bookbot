filepath = "books/frankenstein.txt"

def main():
    booktext = get_file(filepath)
    print(f"--- Report on {filepath} ---")
    # print(count_chars(booktext))
    wordcount = count_words(booktext)
    print(f"Word count: {wordcount}")
    char_dict = count_chars(booktext)
    freq_list = freqs(char_dict)
    
    # print(freq_list)
    for d in freq_list:
        char = d["key"]
        f = d["num"]
        print(f"The '{char}' character was found {f} times")


def get_file(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def count_words(contents):
    wordlist = contents.split()
    return len(wordlist)

def count_chars(contents):
    text = contents.lower()
    char_dict = {}
    for c in text:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1

    return char_dict

def freqs(char_dict):
    dicts = []
    char_keys = list(char_dict)
    # print("length of char_keys: ", len(char_keys))
    for i in range(0, len(char_keys)):
        c = char_keys[i]
        letter = c.isalpha()
        # print(f"i: {i}, char at i: {c}, is alpha? {letter}, number of {char_keys[i]}: {char_dict[char_keys[i]]}")
        
        if c.isalpha():
            dicts.append({ "key": c, "num": char_dict[c] })
    
    dicts.sort(reverse=True, key=sort_on)
    return dicts

def sort_on(dict):
    return dict["num"]



main()
