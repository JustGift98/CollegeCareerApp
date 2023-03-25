import json

from pyahp import parse

with open('model.json') as json_model:
    # model can also be a python dictionary
    model = json.load(json_model)
   #college1 =json.load(json_model)
    #college2 = json.load(json_model)
    #college3 = json.load(json_model)
    #StudyProgram = json.load(json_model)



#reading college lists
#def readColleges(filename = pyAHP.json)


#StudyProgram ={
 #   "Sname":"",
 #   "price":"",
 #   "career":"",
 #   "emp_options": "",
 # "entry_grade": "",
  #  "skills": "",

#}##
"""""
college1 = {
        "name":"Univesity of Botswana",
        "location":"Gaborone",
        "avg_price":"P44000",
        "rank":"30",
        "total_programs ":"250",
        "total_clubs":"27",
        "Campus_type":"Closed with student housing",
        "security_rating":""

}
college1_dict = json.loads(college1)
print(college1_dict)


college2 = {
        "name":"Botswana International University of Science & Technology",
        "location":"Palapye",
        "avg_price":"32000",
        "rank":"187",
        "total_programs ":"71",
        "total_clubs":"x",
        "Campus_type":"Closed with student housing",
        "security_rating":"x"

}
college2_dict = json.loads(college2)
print(college2_dict)



college3 = {
        "name":"Botho University",
        "location":"Gaborone",
        "avg_price":"32000",
        "rank":"322",
        "total_programs ":"31",
        "total_clubs":"x",
        "Campus_type":"Closed with student housing",
        "security_rating":"x"

}

college3_dict = json.loads(college3)
print(college3_dict)
"""

ahp_model = parse(model)
priorities = ahp_model.get_priorities()
