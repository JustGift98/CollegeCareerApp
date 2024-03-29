import json
from itertools import islice

import numpy as np
from django.shortcuts import render, redirect
from pyahp import *

from .forms import *
from .models import *


# homepage when accessing the site before signing up or logging in
def home(request):
    return render(request, 'index.html', {})


# the login page for the web app
def login(request):
    return render(request, 'login.html', {})


def signup(response):
    if response.method == 'POST':
        form = SignUpForm(response.POST)
        if form.is_valid():
            user = form.save()

            # redirect user to home page
            return redirect('dashboard.html')
    else:
        form = SignUpForm()
    return render(response, 'signup.html', {'form': form})


# the page user interacts with after being logged in
def dashboard(request):
    return render(request, 'dashboard.html', {})


def profile(request):
    return render(request, 'profile.html', {})


def college(request):
    return render(request, 'collegesl.html', {})


def program(request):
    return render(request, 'studyprogram.html', {})
"""""
def ahpmodel(request):
    if request.method=='POST':
        criteria =request.POST.getlist('criterion')
        num_criteria = len(criteria)

        #initializing an empty matrix
        pair_matrix = np.zeros((num_criteria,num_criteria))

        for i in range(num_criteria):
            for j in range(num_criteria):
                compare = float(input('How important is' + criteria[i] + 'comapred to '+ criteria[j] + '? (Enter a value between 1-9)'))
                pair_matrix[i][j] = compare
                pair_matrix[j][i] = 1/compare

                #computing the priority vector using AHP
                priority = ahpm.get_priorities(pair_matrix)

                #redirecting to a new page to display the results
                return render(request,'college', priority=priority)
            else:
                form = CompariosonForm()
                return render(request,'college.html', {'form':form})

"""""

def add_crit_model(request):
    if request.method == "POST":
        form = Crit_model_form(request.POST)
        if form.is_valid():
            crit_model = form.save(commit=False)
            crit_model.save()
            return redirect('crit_model_details', pk=crit_model.pk)
    else:
        form = Crit_model_form()
    return render(request, 'college.html', {'form': form})


def crit_model_details(request, pk):
    criteria = Criteria.objects.filter(crit_model=pk).first()
    elements = Element.objects.filter(crit_model=pk).order_by('id')
    decision = json.loads(Crit_model.objects.filter(id=pk).values('decision')[0]['decision'])


    print(decision)
    for element in decision:
        print(element[0])
    return render(request, 'ahp/crit_model_details.html', {'criteria': criteria, 'pk': pk, 'elements': elements, 'decision': decision})


def modify_criterias(request, pk):
    try:
        criteria = Criteria.objects.get(crit_model_id=pk)
        if request.method == "POST":
            form = Criteria_form(request.POST, instance=criteria)
            if form.is_valid():
                criteria = form.save(commit=False)
                criteria.crit_model_id = pk
                criteria.save()
                return redirect('crit_model_details', pk=pk)
        else:
            form = Criteria_form(instance=criteria)
    except:
        if request.method == "POST":
            form = Criteria_form(request.POST)
            if form.is_valid():
                criteria = form.save(commit=False)
                criteria.crit_model_id = pk
                criteria.save()
                return redirect('crit_model_details', pk=pk)
        else:
            form = Criteria_form()

    return render(request, 'ahp/modify_criterias.html', {'form': form})


def modify_elements(request, pk):
    elements = Element.objects.filter(crit_model_id=pk).order_by('id')
    criteria = Criteria.objects.filter(crit_model=pk).first()
    if request.method == "POST":
        form = Element_form(request.POST, request.FILES)
        if form.is_valid():
            element = form.save(commit=False)
            element.crit_model_id = pk
            element.save()
            return redirect('modify_elements', pk=pk)
    else:
        form = Element_form()
    return render(request, 'ahp/modify_elements.html', {'form': form, 'elements': elements, 'criteria': criteria})


def solve(request, pk):
    criteria = Criteria.objects.get(crit_model=pk)
    elements = Element.objects.filter(crit_model=pk)
    # print(elements)

    pairs = []
    for pair in itertools.combinations(
            [[element.name, [element.attrib1, element.attrib2, element.attrib3, element.image]] for element in
             elements], 2):
        pairs.append((pair))

    return render(request, 'ahp/solve.html', {'criteria': criteria, 'pk': pk, 'elements': elements, 'pairs': pairs})


def solver(request, pk):
    response = request.POST.dict()
    response.pop('csrfmiddlewaretoken')
    criteria = list(
        list(Criteria.objects.filter(crit_model=pk).values_list('crit1', 'crit2', 'crit3', 'crit4'))[0])
    alternatives = list(Element.objects.filter(crit_model=pk).values_list('name', flat=True))
    enumerated_alternatives = list(enumerate(alternatives))

    # print(response)
    # here we create matrix for criteria
    array = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    for entry in list(islice(response, 4)):
        if int(response[entry]) < 0:
            array[int(entry[1])][int(entry[0])] = abs(int(response[entry]))
            array[int(entry[0])][int(entry[1])] = 1 / abs(int(response[entry]))
        elif int(response[entry]) == 0:
            array[int(entry[1])][int(entry[0])] = 1
    else:
        array[int(entry[0])][int(entry[1])] = int(response[entry])

    # for x in range(4):
    #     for y in range(4):
#         if array[x][y] == 0:
    #          array[x][y] = 1 / array[y][x]

    criteria_dict = {}
    ilosc_par = int(
        np.math.factorial(len(alternatives)) / (np.math.factorial(2) * np.math.factorial(len(alternatives) - 2)))
    divided_response = {}
    for i in range(6, len(response), ilosc_par):
        divided_response[list(response)[i][0:5]] = list(islice(response.values(), i, i + ilosc_par))

    # print(divided_response)

    for key, entry in divided_response.items():
        temp_arr = []
        for i in range(0, len(alternatives)):
            temp_arr_row = [1] * len(alternatives)
            for j in range(i + 1, len(alternatives)):
                temp_arr_row[j] = int(entry[i])
            temp_arr.append(temp_arr_row)

    for x in range(len(alternatives)):
        for y in range(len(alternatives)):
            if temp_arr[x][y] < 0:
                temp_arr[x][y] = 1 / abs(temp_arr[x][y])
                temp_arr[y][x] = abs(temp_arr[x][y])
            elif temp_arr[x][y] == 0:
                temp_arr[x][y] = 1

    criteria_dict[key] = temp_arr

    print(criteria_dict)

    # print(enumerated_alternatives)
    json_model = json.dumps({"name": "test", "method": "approximate", "criteria": criteria, "subCriteria": {},
                         "alternatives": alternatives, "preferenceMatrices": {"criteria": array,
                                                                              "alternatives:" + criteria[0]:
                                                                                  criteria_dict['crit1'],
                                                                              "alternatives:" + criteria[1]:
                                                                                  criteria_dict['crit2'],
                                                                              "alternatives:" + criteria[2]:
                                                                                  criteria_dict['crit3'],
                                                                              "alternatives:" + criteria[3]:
                                                                                  criteria_dict['crit4'],
                                                                              }})
    print(json_model)
    model = json.loads(json_model)
    # try:
    #     ahp_model = parse(model)
    #     priorities = ahp_model.get_priorities()
    #     print(priorities)
    # except AssertionError as error:
    #     print(error)
    # priorities = ahp_model.get_priorities()
    ahp_model = parse(model)
    priorities = ahp_model.get_priorities()
    result = list(zip(alternatives, priorities))
    Crit_model.objects.filter(id=pk).update(decision=json.dumps(result))
    print(result)
    return redirect('crit_model_details', pk=pk)

