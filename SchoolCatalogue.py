# Let’s put your knowledge of classes to the test by creating a digital school
# catalog for the New York City Department of Education. The Department of
# Education wants the catalog to hold quick reference material for each school
# in the city.

# We need to create classes for primary and high schools. Because these classes
# share properties and methods, each will inherit from a parent School class.
# Our parent and three child classes have the following properties,
# getters, setters, and methods.

# School:
# Properties: name (string), level (one of three strings: 'primary',
# 'middle', or 'high'), and numberOfStudents (integer)
# Getters: all properties have getters
# Setters: the numberOfStudents property has a setter
# Methods: A __repr__ method that displays information about the school.

# Primary
# Includes everything in the School class, plus one additional property
# Properties: pickupPolicy (string, like "Pickup after 3pm")

# Middle
# Does not include any additional properties or methods

# High
# Includes everything in the School class, plus one additional property
# Properties: sportsTeams (list of strings, like ['basketball', 'tennis'])


# Create the School Class
class School:
    def __init__(self, name, level, number_of_student):
        if not isinstance(name, str):
            raise TypeError("name must be str")
        if not (level == "primary" or level == "middle" or level == "high"):
            raise TypeError("level must be \"primary\", \"middle\" or \"high\"")
        if not isinstance(number_of_student, int):
            raise TypeError("number_of_student must be int")

        self.name = name
        self.level = level
        self.number_of_student = number_of_student

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_student_num(self):
        return self.number_of_student

    def __repr__(self):
        return f"A {self.level} school named {self.name} with " \
               f"{self.number_of_student} students"


# school test
school_test = School("School Test", "middle", 0)
print(school_test)

school_test.name = "School Test 2"
print(school_test.get_name())

school_test.level = "primary"
print(school_test.get_level())

school_test.number_of_student = 10
print(school_test.get_student_num())

print()


# Create PrimarySchool Class
class PrimarySchool(School):
    def __init__(self, name, number_of_student,
                 pickup_policy="Pick up after 3pm"):
        super().__init__(name, "primary", number_of_student)

        if not isinstance(pickup_policy, str):
            raise TypeError("pickup_policy must be str")
        self.pickup_policy = pickup_policy

    def get_pickup_policy(self):
        return self.pickup_policy

    def __repr__(self):
        return super().__repr__() + f"\nPickup policy: {self.pickup_policy}"


# primary school test
primary_school_test = PrimarySchool("Primary School Test", 0)
print(primary_school_test)

primary_school_test.pickup_policy = "Pick up After 4pm"
print(primary_school_test.get_pickup_policy())

print()


# Create HighSchool Class
class HighSchool(School):
    def __init__(self, name, number_of_student, sports_teams=None):
        super().__init__(name, "high", number_of_student)

        if sports_teams is None:
            sports_teams = []
        self.sports_teams = sports_teams

    def get_sports_teams(self):
        return self.sports_teams

    def add_sports_team(self, team):
        self.sports_teams.append(team)

    def __repr__(self):
        return super().__repr__() + f"\nSports Teams: {self.sports_teams}"


# high school test
high_school_test = HighSchool("High School Test", 0)
print(high_school_test)

high_school_test.add_sports_team("team1")
high_school_test.add_sports_team("team2")
print(high_school_test.get_sports_teams())


# empty line
