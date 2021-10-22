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
    def __init__(self, name, level, numberOfStudents):
        if not isinstance(name, str):
            raise TypeError("name must be str")
        if not (level == "primary" or level == "middle" or level == "high"):
            raise TypeError("level must be \"primary\", \"middle\" or \"high\"")
        if not isinstance(numberOfStudents, int):
            raise TypeError("numberOfStudent must be int")

        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents


# school test
School("test_school", "middle", 0)



# empty line
