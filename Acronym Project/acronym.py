#Here the variable testStr is set to a string that we want to get the acronyms for.
testStr = "Absent Without Leave"

"""
strList is assigned to the original string after it is split
into a list using the method split and it is split around spaces.
"""

strList = testStr.split(" ")

#We are creating a variable called acronym and assinging it an empty string.
acronym = ""

"""
We are iterating over every element in the list.
"""
for str in strList:
    """
    The acronym variable is concatenated with the first letter from each word.
    """
    acronym += str[0]

#The acronym is made upper case using the upper method and then printed.	
print(acronym.upper())
