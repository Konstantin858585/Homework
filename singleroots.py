def single_root_words(root_word,*other_words):
    words = input('ведите список слов через запятую :', )
    words.lower()
    other_words = words.split(',')
    same_words = list()
    for i in range (len(other_words)):
        if root_word in other_words[i]:
            same_words.append(other_words[i])


    print(same_words)


single_root_words(root_word=input('введите искомое слово:', ).lower(), )