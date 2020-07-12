# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def create_mask(censor):
    censored_mask = ""
    for i in range(len(censor)):
        if censor[i] == " ":
            censored_mask = censored_mask + " "
        else:
            censored_mask = censored_mask + "X"
    return censored_mask

def censor_text(text,censor):
    censored_mask = create_mask(censor)
    censored_text = text.replace(censor,censored_mask)
    censored_text = censored_text.replace(censor.capitalize(),censored_mask)
    return censored_text

def censor_list_of_text(text,censor):
    for entry in censor:
       text = censor_text(text,entry)
    return text

def censor_negative(text,censor,negative):
    #TODO #4 This needs to be updated to support negative phrases
    for char in puctuation:
        text = text.replace(char, ' ' + char)
    split_text = text.split()
    neg_count = 0
    new_text = ""
    for i in range(len(split_text)):
        censored_text = ""
        puntuation_flag = False
        for neg_word in negative:
            if split_text[i] == neg_word and neg_count >= 2:
                #print(neg_word + ": " + split_text[i])
                censored_text = create_mask(split_text[i])
                #print(censored_text)
                neg_count += 1
            elif split_text[i] == neg_word:
                censored_text = split_text[i]
                neg_count += 1
        if censored_text:
            new_text = new_text + " " + censored_text
        else:
            for char in puctuation:
                if split_text[i] == char:
                    puntuation_flag = True
                    break
            if puntuation_flag or i == 0:
                new_text = new_text + split_text[i]
            else:
                new_text = new_text + " " + split_text[i]
    return censor_list_of_text(new_text,censor)

puctuation = [",","."]
term = "learning algorithms"
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable"]
test_phrase = "I am concerned that this project is horrible, awful, and broken."

#print(censor_text(email_one,term))
#print(censor_list_of_text(email_two,proprietary_terms))
print(censor_negative(email_three,proprietary_terms,negative_words))