# from fuzzywuzzy import fuzz



def clearTitle(Title):
    returnedTitle = ""
    position = Title.find("(")
    if position != -1:
        if Title[position+1].lower() == "f" and Title[position+2].lower() == "e":
            for i in range(position):
                returnedTitle = returnedTitle + Title[i]
            return returnedTitle
    return Title

x = "Hello - Adele (live)"

print(clearTitle(x))