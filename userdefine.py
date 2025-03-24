def employee_details(name, salary, job="Unknown", *extra):
    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Job: {job}")
    print(f"Extra Info: {extra}")# Captures any additional values

# Example calls
employee_details("Alice", 50000)# Uses default job
employee_details("Bob", 60000, "Developer")# passing value
employee_details("Charlie", 70000, "Manager", 30)# Extra value goes into *extra
