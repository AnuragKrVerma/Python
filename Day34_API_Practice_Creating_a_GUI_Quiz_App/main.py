# datatype

age: int
name: str
Abc: bool

# type hint
def can_drive(age: int)-> bool:
    if (age>18):
        drive = False
    else:
        drive = True
    
    return drive
