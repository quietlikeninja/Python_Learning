# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_text(text,censor):
    censored_mask = ""
    for i in range(len(censor)):
        if censor[i] == " ":
            censored_mask = censored_mask + " "
        else:
            censored_mask = censored_mask + "X"
    censored_text = text.replace(censor,censored_mask)
    censored_text = censored_text.replace(censor.capitalize(),censored_mask)
    return censored_text

def censor_list_of_text(text,censor):
    for entry in censor:
       text = censor_text(text,entry)
    return text

def censor_negative(text,censor):
    count = 0
    censored_text = ""
    for word in text:
        print(word)
        for entry in censor:
            if word == entry and count != 2:
                censored_text = censored_text + word
                count += 1
            elif word == entry:
                censored_text = censored_text + censor_text(word,entry)
    return censored_text


term = "learning algorithms"
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

#print(censor_text(email_one,term))
print(censor_list_of_text(email_two,proprietary_terms))
#print(censor_three("I am concerned that this project is horrible, awful, and broken.",proprietary_terms,negative_words))