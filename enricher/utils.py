import json





def bringing_lists_from_json():
    with open('data/pizza_analysis_lists.json', 'r') as file:
        data = json.load(file)
        return data



def compatibility_check(note,text):
    for row in note:
        if row.upper() in text:
            return True
    return False


def update_new_fields(data):
    data['is_allergic'] = False
    data['is_kosher'] = True
    data['is_meat'] = False
    data['is_dairy'] = False
    data['is_vegan'] = True
    data['status'] = 'DELIVERED'

    keys = ["is_allergic","is_kosher","is_meat","is_dairy"]
    lists = bringing_lists_from_json()
    for note,key in zip(lists ,keys):
        is_changed = False
        note_value = lists.get(note)
        if compatibility_check(note_value,data['clean_pizza_prep']):
            if not is_changed:
                data[key] = not(data[key])
                is_changed = True

    if data['is_meat'] and data['is_dairy']:
        data['is_kosher'] = False

    if data['is_meat'] or data['is_dairy']:
        data['is_vegan'] = False

    if not data['is_kosher']:
        data['status'] = 'BURNT'

    return data








