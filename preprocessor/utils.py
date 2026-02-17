import string
import json

def clearing_the_data(data):
    translator = str.maketrans('', '', string.punctuation)
    clean_text = data.translate(translator)
    data = clean_text.upper()
    return data



def pulling_out_pizza_prep(pizza_type):
    with open("data/pizza_prep.json","r") as file:
        data = json.load(file)
        pizza_prep = data.get(pizza_type,'')
        return pizza_prep



