def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
       person_list = [f"{katz_deli.index(person) + 1}. {person}" for person in katz_deli]
       print(f"The line is currently: {' '.join(person_list)}")
       

def take_a_number(katz_deli, persons_name):
    katz_deli.append(persons_name)
    print(f"Welcome, {persons_name}. You are number {katz_deli.index(persons_name) + 1} in line.")


def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli.pop(0)}.")
        

