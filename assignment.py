import time

def college_application():
    # Collecting student details
    student_name = input("Enter Student Name: ")
    father_name = input("Enter Father's Name: ")
    mother_name = input("Enter Mother's Name: ")
    occupation1 = input("Enter Father's Occupation: ")
    occupation2 = input("Enter Mother's Occupation: ")
    annual_income = int(input("Enter Annual Income: "))
    first_graduate = input("Are you the first graduate in the family? (yes/no): ")
    date_of_birth = input("Enter Date of Birth (DD/MM/YYYY): ")
    age = int(input("Enter Age: "))
    mobile_no = input("Enter your Mobile Number: ")
    email = input("Enter your Email Address: ")
    total_marks = int(input("Enter your total marks out of 600: "))
    percentage = (total_marks / 600) * 100
    print("Your percentage is:", percentage)
    group = input("Enter your +2 group (Commerce / Computer Science / Biology / Pure Science): ")
    college_name = input("Which college to apply to: ")
    district = input("Enter college District: ")
    
    # Determining course eligibility
    if percentage >= 50:
        degree = input("Choose your degree (Engineering / Arts and Science): ")
    else:
        print("Your percentage is below 50%. You are eligible only for Arts and Science.")
        degree = "Arts and Science"
    
    # Course selection
    engineering_departments = ["1. Information Technology", "2. Computer Science", "3. Electrical and Electronics", "4. Electrical Communication", "5. Biotechnology", "6. Pharmaceutical", "7. Mechanical", "8. Civil", "9. Automobile"]
    arts_science_departments = ["1. BBA", "2. BCA", "3. Fashion Technology", "4. Catering", "5. BSc Nursing", "6. BA Tamil", "7. BA English", "8. BSc Maths", "9. Microbiology"]
    
    if degree.lower() == "engineering" and group.lower() in ["biology", "computer science"]:
        print("Choose your Engineering Department:")
        for dept in engineering_departments:
            print(f"- {dept}")
        course = input("Enter your choice: ")
        if course not in engineering_departments:
            print("Invalid choice. Defaulting to CSE.")
            course = "Computer Science"
    else:
        print("Choose your Arts and Science Department:")
        for dept in arts_science_departments:
            print(f"- {dept}")
        course = input("Enter your choice: ")
        if course not in arts_science_departments:
            print("Invalid choice. Defaulting to BSc Maths.")
            course = "BSc Maths"
    
    # Displaying student details
    print("\n--- College Application Details ---")
    print(f"Student Name: {student_name}")
    print(f"Father's Name: {father_name}")
    print(f"Mother's Name: {mother_name}")
    print(f"Father's Occupation: {occupation1}")
    print(f"Mother's Occupation: {occupation2}")
    print(f"Annual Income: {annual_income}")
    print(f"First Graduate: {first_graduate}")
    print(f"Date of Birth: {date_of_birth}")
    print(f"Age: {age}")
    print(f"Mobile Number: {mobile_no}")
    print(f"Email Address: {email}")
    print(f"Total Marks: {total_marks}/600")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Group: {group}")
    print(f"College Name: {college_name}")
    print(f"District: {district}")
    print(f"Degree Chosen: {degree}")
    print(f"Department Allotted: {course}")
    
    # Simulating allotment order delay
    print("\nProcessing your application...")
    time.sleep(2)  # Simulating 2 days delay with a shorter wait
    print("\nAllotment order will be received after 2 days via email.")
    print("Congratulations! You have successfully applied for the college.")

# Running the program
college_application()
