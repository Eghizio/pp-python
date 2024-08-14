import random
import time

def rnd(): return random.randint(1, 999_000_000) + int(time.time())


# with open("./files/data.csv") as file:
#     data = file.read() 
#     print(data)


# def parse_line(line):
#     return [word.strip() for word in line.split(",")]

# def make_dict(keys, values):
#     d = {}
#     for k, v in zip(keys, values):
#         d[k] = v
#     return d

# def parse_employees(filepath):
#     with open(filepath, "r") as file:
#         data = file.readlines()
#         keys = parse_line(data[0])
#         employees = [make_dict(keys, parse_line(line)) for line in data[1:]]
#         return employees
    
# file_path = "./files/data.csv"
# employees = parse_employees(file_path)

# # print(employees)
# for e in employees:
#     print(e)
    

# with open(f"./files/_output_{rnd()}.txt", "w") as f: 
#     f.write(f"Hello World!!! {rnd()}")



# with open(f"./files/_output.txt", "a") as f: 
#     f.write(f"Hello There!!! {rnd()}")





import json

JSON_DATA =  '{ "name":"John", "age":30, "city":"New York" }'
data = json.loads(JSON_DATA)
print(data["age"])


some_set = {5,4,3,2,1,1}
print(some_set)
print(some_set)

# data["age"] += 1
# JSON_DATA = json.dumps(data, indent=4)
# print(JSON_DATA)

# with open(f"./files/john.json", "w") as f: 
#     f.write(JSON_DATA)



# def increase_salaries_report(amount, csv_file = "./files/data.csv"):
#     employees = []
    
#     with open(csv_file) as f:
#         data = f.readlines()
        
#         for line in data[1:]:
#             values = [word.strip() for word in line.split(",")]
#             id,name,age,email,salary = values
            
#             salary = int(salary) + amount

#             entry = {
#                 "id": id,
#                 "name": name,
#                 "age": age,
#                 "email": email,
#                 "salary": salary,
#             }

#             employees.append(entry)
        
#     serialized_data = json.dumps(employees, indent=2)
#     with open(f"./files/_report_{rnd()}", "w") as report:
#         report.write(serialized_data)
#         print("Report generated!")

# increase_salaries_report(800, "./files/data.csv")

# # Challenge:
# # Create a simple game and save highscores to File.
# # It should contain: Date, Name, Score.
# # Allow program to read top Leaderboard (top 3 or 10 etc.)
