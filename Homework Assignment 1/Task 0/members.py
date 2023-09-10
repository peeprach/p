team_members = [
    {"name": "Prach Changpradit", "student_id": "6422770170"},
    {"name": "C้haiyaboon Taysint", "student_id": "6422771160"},
    
]

def print_team_members():
    for member in team_members:
        print(f"Name: {member['name']}, Student ID: {member['student_id']}")

if __name__ == "__main__":
    print_team_members()