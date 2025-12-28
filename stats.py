def word_count(file_contents):

    count = 0
    for word in file_contents.split():

        if word:
            count += 1

    return count

def character_count(file_contents):

    word_list = file_contents.split()

    character_dict = {}
    for word in word_list:

        for character in word.lower():

            if character in character_dict:

                character_dict[character] += 1
            else:
                character_dict[character] = 1
    
    return character_dict

def sort_on(items):

    return items["num"]

def sorted_dicts(dict_of_chars):

    dict_list = []
    for character in dict_of_chars:

        new_dict = {"char": character, "num": dict_of_chars[character]}
        dict_list.append(new_dict)

    dict_list.sort(reverse=True, key=sort_on)
    
    return dict_list    