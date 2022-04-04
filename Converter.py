from pathlib import *

breaking_point = "yes"
while(True):
    if(breaking_point == "yes"):
        where_name = input("In which folder do you want to convert? " )
        type_name = input("What type do you want to convert your files to? ").lower()
        path = Path(f"{where_name}")
        duplicate_number = 1
        for x in path.iterdir():
            x_str = x.__str__()
            dot_index = x_str.index(".")
            x_str = x_str[0:dot_index]
            try:
                x.rename(x_str + "." + type_name)
            except FileExistsError:
                x.rename(f"{x_str}({duplicate_number.__str__()}).{type_name}")
                duplicate_number += 1
    else:
        print("Thanks for converting!")
        break
    breaking_point = input("Do you want to convert again? ").lower()

