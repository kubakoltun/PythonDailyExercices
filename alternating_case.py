def to_alternating_case(string):
    news = ''
    for i in range (len(string)):
        if(string[i].islower()):
            news += string[i].upper()
        else:
            news += string[i].lower()
    return news
