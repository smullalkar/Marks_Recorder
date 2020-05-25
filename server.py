from flask import Flask
from flask import request
from flask_cors import CORS
import json
import csv

app = Flask(__name__)
CORS(app)

@app.route('/allstudents')
def studentList():
    csv_file = open('data/students.csv', 'r')
    csvreader = csv.DictReader(csv_file)

    rows = []
    for row in csvreader:
        rows.append(row)

    csv_file.close()
    return json.dumps(rows)


@app.route("/addstudent", methods = ["POST"])
def create():
    name = request.json["name"]
    class_of_student = request.json["class_of_student"]
    roll_no = request.json["roll_no"]
    section = request.json["section"]
    exam_type = request.json["exam_type"]
    maths = request.json["maths"]    
    soc_science = request.json["soc_science"]    
    science = request.json["science"]    
    english = request.json["english"]    
    hindi = request.json["hindi"]    
    second_language = request.json["second_language"]    
    total_min = request.json["total_min"]
    total_max = request.json["total_max"]
    
    math = float(maths)
    sst = float(soc_science)
    sc = float(science)
    eng = float(english)
    hin = float(hindi)
    sec_l = float(second_language)
    total_marks_obtained = float(math+sst+sc+eng+hin+sec_l)
    
    tot_min = float(total_min)
    tot_max = float(total_max)
    
    max_marks_of_each_sub = float(tot_max/6)
    minimium_to_pass = float(float(max_marks_of_each_sub)*0.4)
    
    percent = float((total_marks_obtained*100)/tot_max) 
    
    if (percent >= 80) :
        grade = 'O'
    elif (percent >= 75) and  (percent < 80):
        grade = 'A'
    elif (percent >= 70) and  (percent < 75):
        grade = 'B'
    elif (percent >= 60) and  (percent < 70):
        grade = 'C'
    elif (percent >= 50) and  (percent < 60):
        grade = 'D'
    elif (percent >= 45) and  (percent < 50):
        grade = 'E'
    elif (percent >= 40) and  (percent < 45):
        grade = 'PASS'
    elif (percent < 40):
        grade = 'FAIL'
        
    if math >= minimium_to_pass and sst >= minimium_to_pass and sc >= minimium_to_pass and eng >= minimium_to_pass and hin >= minimium_to_pass and sec_l >= minimium_to_pass :
        final_grade = grade
    else:
        final_grade = 'FAIL'
            
    data = {
        "name": name,
        "class_of_student":class_of_student,
        "roll_no": roll_no,
        "section": section,
        "exam_type": exam_type,
        "maths": maths,
        "soc_science": soc_science,
        "science": science,
        "english": english,
        "hindi": hindi,
        "second_language": second_language,
        "total_min": total_min,
        "total_max": total_max,
        "grade": final_grade,
        "total_marks_obtained": total_marks_obtained,
        "percent": percent,
        "max_marks_each_sub": float(max_marks_of_each_sub),
        "min_marks_each_sub": float(minimium_to_pass)
    }    
    
    new_data = []    
    latest_id = 0    
    
    #read data here
    student_csv_file = open("data/students.csv", "r")    
    csvreader = csv.DictReader(student_csv_file)    
    for i in csvreader:
        latest_id = i["id"]
        new_data.append(i)    
    student_csv_file.close() 
       
    data["id"] = float(latest_id) + 1    
    new_data.append(data)
        
    #write data here
    handle_csv = open("data/students.csv", "w")    
    header = data.keys()    
    writers = csv.DictWriter(handle_csv, fieldnames=header)    
    writers.writeheader()
    writers.writerows(new_data)    
    handle_csv.close()    
    return {"student_added": True, "message": "successful"}

@app.route('/allstudents/student/<id>')
def show(id):
    target = id
    csv_file = open('data/students.csv','r')
    csvreader = csv.DictReader(csv_file)
    
    user_data = []
    
    for row in csvreader:
        if row['id'] == target:
            user_data.append(row)
            
    return json.dumps(user_data)

@app.route('/class1')
def class1():
    target = id
    csv_file = open('data/students.csv','r')
    csvreader = csv.DictReader(csv_file)
    
    user_data = []
    
    for row in csvreader:
        if row['class_of_student'] == '1':
            user_data.append(row)
            
    return json.dumps(user_data)

@app.route('/class2')
def class2():
    target = id
    csv_file = open('data/students.csv','r')
    csvreader = csv.DictReader(csv_file)
    
    user_data = []
    
    for row in csvreader:
        if row['class_of_student'] == '2':
            user_data.append(row)
            
    return json.dumps(user_data)

@app.route('/class3')
def class3():
    target = id
    csv_file = open('data/students.csv','r')
    csvreader = csv.DictReader(csv_file)
    
    user_data = []
    
    for row in csvreader:
        if row['class_of_student'] == '3':
            user_data.append(row)
            
    return json.dumps(user_data)

@app.route('/class4')
def class4():
    target = id
    csv_file = open('data/students.csv','r')
    csvreader = csv.DictReader(csv_file)
    
    user_data = []
    
    for row in csvreader:
        if row['class_of_student'] == '4':
            user_data.append(row)
            
    return json.dumps(user_data)

@app.route('/class5')
def class5():
    target = id
    csv_file = open('data/students.csv','r')
    csvreader = csv.DictReader(csv_file)
    
    user_data = []
    
    for row in csvreader:
        if row['class_of_student'] == '5':
            user_data.append(row)
            
    return json.dumps(user_data)

@app.route('/class6')
def class6():
    target = id
    csv_file = open('data/students.csv','r')
    csvreader = csv.DictReader(csv_file)
    
    user_data = []
    
    for row in csvreader:
        if row['class_of_student'] == '6':
            user_data.append(row)
            
    return json.dumps(user_data)

@app.route('/class7')
def class7():
    target = id
    csv_file = open('data/students.csv','r')
    csvreader = csv.DictReader(csv_file)
    
    user_data = []
    
    for row in csvreader:
        if row['class_of_student'] == '7':
            user_data.append(row)
            
    return json.dumps(user_data)

@app.route('/class8')
def class8():
    target = id
    csv_file = open('data/students.csv','r')
    csvreader = csv.DictReader(csv_file)
    
    user_data = []
    
    for row in csvreader:
        if row['class_of_student'] == '8':
            user_data.append(row)
            
    return json.dumps(user_data)

@app.route('/class9')
def class9():
    target = id
    csv_file = open('data/students.csv','r')
    csvreader = csv.DictReader(csv_file)
    
    user_data = []
    
    for row in csvreader:
        if row['class_of_student'] == '9':
            user_data.append(row)
            
    return json.dumps(user_data)

@app.route('/class10')
def class10():
    target = id
    csv_file = open('data/students.csv','r')
    csvreader = csv.DictReader(csv_file)
    
    user_data = []
    
    for row in csvreader:
        if row['class_of_student'] == '10':
            user_data.append(row)
            
    return json.dumps(user_data)

@app.route('/filter/examtype/<exam_type>')
def filter_examtype(exam_type):
    target = exam_type
    csv_file = open('data/students.csv','r')
    csvreader = csv.DictReader(csv_file)
    
    user_data = []
    
    if target == 'All':
        for row in csvreader:
            user_data.append(row)
    else:
        for row in csvreader:
            if row['exam_type'] == target:
                user_data.append(row)
            
    return json.dumps(user_data)

# @app.route('/users/edit/<id>', methods=['POST'])
# def edit(id):    
    
#     name = request.json["name"]
#     email = request.json["email"] 
#     mobile = request.json["mobile"]
#     age = request.json["age"]
       
#     data = {
#         "name": name,
#         "email": email,
#         "mobile": mobile,
#         "age": age,
#         "id" : id
#     } 
    
#     csv_file = open('data/users.csv','r')
#     csvreader = csv.DictReader(csv_file)     
    
#     target = id   
#     new_data = []    
       
#     for i in csvreader:
#         if id == i['id']:
#             new_data.append(data)
#         else:
#             new_data.append(i)
#     csv_file.close() 
       
#     csv_file = open("data/users.csv", "w")    
#     header = new_data[0].keys()    
#     write_data = csv.DictWriter(csv_file, fieldnames=header)    
#     write_data.writeheader()
#     write_data.writerows(new_data)    
#     csv_file.close()    
#     return json.dumps(new_data)

# @app.route('/users/delete/<id>', methods=['POST'])
# def delete(id):
#     target = id    
#     new_data = []    
#     csv_file = open("data/users.csv", "r")    
#     csvreader = csv.DictReader(csv_file)    
#     for i in csvreader:
#         if i['id'] == id:
#             pass
#         else:
#             new_data.append(i)
#     csv_file.close() 
       
#     csv_file = open("data/users.csv", "w")    
#     header = new_data[0].keys()   
#     write_data = csv.DictWriter(csv_file, fieldnames=header)    
#     write_data.writeheader()
#     write_data.writerows(new_data)   
#     csv_file.close()    
#     return json.dumps({"data": str(new_data), "response":"user successfully deleted"})