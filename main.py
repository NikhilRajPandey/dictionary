# creating a dictonary
new_dict = {"trouble":"problem",
            "c++":"computer language",
            "update":"a new change",
            "code with harry":"youtube-channel",
            "hindustani supporter":"fan of harry sir"
            }

# if input founds
try:
    # taking inputs from the user
    inp1 = input("word:")

    # making non-case sensitive
    lowerinput = inp1.lower()

    # giving output to user
    for keys in new_dict:
        resultskeys = keys.find(lowerinput)
        if resultskeys != -1:
            print(keys)

# if input not founds
except:
    print("No found")