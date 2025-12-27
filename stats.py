def count_words(text):
    words = text.split()
    num_words = len(words)
    return f"Found {num_words} total words"

def count_chars(text):
    count = {}
    words = text.lower()
    for char in words:
        if char not in count:
            count[char] = 1
        else:
            count[char] +=1
    return count

def sort_on(items):
    return items["num"]
 

def sort_dict(items):
    listed = []
    for k in items:
        listed.append({"char": k, "num": items[k]})
    listed.sort(reverse=True,key=sort_on)
    #print(sorted)
    #print(listed)
    return listed

def report(filepath, text):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(count_words(text))
    print("--------- Character Count -------")
    for i in sort_dict(count_chars(text)):
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")


