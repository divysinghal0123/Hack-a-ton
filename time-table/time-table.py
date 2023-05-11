import random

# Define constants
NUM_PERIODS_PER_DAY = 7
NUM_DAYS_PER_WEEK = 6
BREAK_PERIODS = [2, 4]

# Take inputs for number of subjects
num_theory_subjects = int(input("Enter the number of theory subjects: "))
num_analytic_subjects = int(input("Enter the number of analytic subjects: "))
num_lab_slots = int(input("Enter the number of lab slots per week: "))

# Define subject list with details
subject_list = []
for i in range(num_theory_subjects):
    subject_list.append({"name": f"Theory Subject {i+1}", "type": "theory", "num_sessions": 0})
for i in range(num_analytic_subjects):
    subject_list.append({"name": f"Analytic Subject {i+1}", "type": "analytic", "num_sessions": 0})
for i in range(num_lab_slots):
    subject_list.append({"name": f"Lab Subject {i+1}", "type": "lab", "num_sessions": 0})

# Define timetable
timetable = []
for i in range(NUM_DAYS_PER_WEEK):
    day = []
    for j in range(NUM_PERIODS_PER_DAY):
        day.append("")
    timetable.append(day)

# Assign a first period for each subject randomly on any day of the week
for subject in subject_list:
    day = random.randint(0, NUM_DAYS_PER_WEEK-1)
    period = random.randint(0, 1)
    timetable[day][period] = subject["name"]
    subject["num_sessions"] += 1

# Assign two consecutive periods for analytic subjects on any day of the week
for subject in subject_list:
    if subject["type"] == "analytic":
        assigned = False
        while not assigned:
            day = random.randint(0, NUM_DAYS_PER_WEEK-1)
