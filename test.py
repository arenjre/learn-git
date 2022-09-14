names = ["akash", "ajay", "nisha", "ranu", "saumitra", "sandhya", "yamini"]
def process_bonus(name):
    print("Bonus has been processed for.....", name)
def process_salary(name):
    print("Salary has been processed for++++++++++++", name)
# Please use the above function assume that they are part of a larger codebase
# They have been written here for your simplification.
# Do not modify the function which I have written.
# Do not override the function just re-use th
def show():
    names = ["akash", "ajay", "nisha", "ranu", "saumitra", "sandhya", "yamini"]
    for i in names:
        process_salary(i)
        if i.startswith('s'):
            continue
        process_bonus(i)
show()