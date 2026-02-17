import json

x = {'order_id': 'order_1012', 'pizza_type': 'Pepperoni'
    , 'clean_special_instructions': 'COORDINATES 320853 N 347818'
                                    ' E 15 MINS DELAY DUE TO HEAVY PATROLS'
    , 'clean_pizza_prep': 'PREHEAT OVEN TO 220°C 425°F BAKE FOR 1215 MINUTES UNTIL '
                          'CHEESE IS MELTED AND PEPPERONI EDGES ARE SLIGHTLY CRISPY '
                          'FOR FROZEN PIZZA DO NOT THAW BAKE DIRECTLY FROM FROZEN FOR '
                          '1518 MINUTES PLACE DIRECTLY ON OVEN RACK OR USE A PIZZA STONE'
                          ' FOR CRISPIER CRUST ROTATE PIZZA HALFWAY THROUGH BAKING FOR'
                          ' EVEN COOKING LET REST FOR 23 MINUTES BEFORE'
                          ' SLICING TO ALLOW CHEESE TO SET KEEP'
                          ' REFRIGERATED OR FROZEN UNTIL READY'
                          ' TO COOK WASH HANDS AFTER HANDLING'
                          ' RAW DOUGH OR PACKAGING CLEAN C'
                          'UTTING BOARD AND PIZZA CUTTER AFTER USE'}


def bringing_lists_from_json():
    with open('data/pizza_analysis_lists.json', 'r') as file:
        data = json.load(file)
        return data


def compatibility_check(text,note):
    for row in note:
        if row in text:
            return True
    return False



def update_new_fields(data,text):
    data['is_meat'] = False
    data['is_dairy'] = True
    data['is_kosher'] = True
    data['is_allergic'] = False
    keys = ["is_allergic","is_kosher","is_meat","is_dairy"]
    lists = bringing_lists_from_json()
    for note,key in zip(lists ,keys):
        note_value = lists.get(note)
        for single_note in note_value:
            if single_note in text:
                data[key] = not(data[key])
    if data['is_meat'] and data['is_dairy']:
        data['is_kosher'] = False
    return data

print(update_new_fields(x,"salami"))


