class User:
    def __init__(self, name, nationality, dob):
        self.name = name
        self.nationality = nationality
        self.dob = dob

    def __str__(self):
        return f"Name: {self.name} | Nationality: {self.nationality}\t | DOB: {self.dob}"