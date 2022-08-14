def lyrics_generator(items):
    one_counter = 0
    lyrics = ""

    for i in items:
        if i == 0:
            lyrics += "Boom "
            one_counter = 0
        elif i == 1:
            lyrics += "Drop the base "
            one_counter += 1

            if one_counter == 3:
                lyrics += "!!!Break the base!!! "
                one_counter = 0
    
    return lyrics

# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))