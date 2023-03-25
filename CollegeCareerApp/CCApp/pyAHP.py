import json
from pyahp import parse
from models import College,StudyProgram

with open('model.json') as json_model:
    # model can also be a python dictionary
    model = json.load(json_model)

ahp_model = parse(College)
priorities = ahp_model.get_priorities()
