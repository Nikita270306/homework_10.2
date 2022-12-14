import json
def load_candidates():
    with open("candidates.json.", "r") as candidates:
        return json.load(candidates)


def get_by_pk(pk):
    return load_candidates()[pk - 1]


def get_by_skill(skill_name):
    for i in load_candidates():
        if skill_name.lower() in i['skills'].lower():
            return i


def information(all_information):
    strok = ''
    for i in range(len(all_information)):
        strok += f'''
        Имя кандидата - {all_information[i]["name"]}
        Позиция кандидата - {all_information[i]["position"]}
        Навыки - {all_information[i]["skills"]}
        '''
    return f'<pre>{strok}</pre>'



