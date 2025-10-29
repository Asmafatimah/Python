class_info = {
    "class_name": "CSE(AI)",
    "semester": 3,
    "subject": "SAC LAB"
    }


students = [
      {"name" : "Asma Fatimah", "roll_no": 70},
      {"name" : "Safiya Ruhi", "roll_no": 73},
      {"name" : "Azra Umaimah", "roll_no": 68}
      ]
def display_class_info():
      print("Class information:")
      for key,value in class_info.items():
          print(f"{key.capitalize()} : {value}")
def display_students():
    print("\n Students List:")
    for s in students:
        print(f"Roll no: {s['roll_no']} - Name: {s['name']}")





