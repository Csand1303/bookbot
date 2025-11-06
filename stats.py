def count_words(book):
    words = book.split()
    word_count = len(words)
    return word_count

def count_characters(book):
    dict = {}
    book = book.lower()
    for chr in book:
        if chr in dict:
            dict[chr] += 1
        else:
            dict[chr] = 1
    return dict 

def report(charetors):
    result = []
    for chr, count in charetors.items():
        if chr.isalpha():
            result.append({"char": chr, "num": count})
        result.sort(key=sort_on, reverse=True)
    return result        

def sort_on(item):
    return item["num"]