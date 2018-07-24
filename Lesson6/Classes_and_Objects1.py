class Firefox:
    """This Class is accepting the input from the
    user and giving output"""
    def __init__(self,computer1,computer2):
        self.comp1Name = computer1
        self.comp2Name = computer2
print("Enter Table 1 Computer Names")
table1 = Firefox(str(input()),str(input()))

print("Enter Table 2 Computer Names")
table2 = Firefox(str(input()),str(input()))

print(table1.comp1Name)
print(table2.comp1Name)

print(table1.comp2Name)
print(table2.comp2Name)

help(Firefox)