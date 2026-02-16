import string



def search_in_text(data):
    if "allergy" in data["special_instructions"].lower() or \
            "peanut" in data["special_instructions"].lower() or\
            "gluten" in data["special_instructions"].lower():
        data["allergies_flagged"] = True
    else:
        data["allergies_flagged"] = False

    return data


def clearing_the_data(data):
    translator = str.maketrans('', '', string.punctuation)
    clean_text = data["special_instructions"].translate(translator)
    data["cleaned_protocol"] = clean_text.upper()
    return data





