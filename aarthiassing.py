def college_application():
    #student details
    print("!--COLLEGE APPLICATION--!")
    student_name = input("Enter Student Name: ")
    father_name = input("Enter Father's Name: ")
    mother_name = input("Enter Mother's Name: ")
    occupation1 = input("Enter Father's Occupation: ")
    occupation2 = input("Enter Mother's Occupation: ")
    community=input("Enter your community:")
    annual_income = int(input("Enter Annual Income: "))
    first_graduate = input("Are you the first graduate in the family? (yes/no): ").strip().lower()
    #scholarship details
    if first_graduate == "yes":
        print("You are eligible for a scholarship, and the total fees will be reduced by a certain amount!")
    else:
        print("You are not a first graduate, so no scholarship is available.")

    date_of_birth = input("Enter Date of Birth (DD/MM/YYYY): ")
    age = int(input("Enter Age: "))
    mobile_no = input("Enter your Mobile Number: ")
    email = input("Enter your Email Address: ")
    total_marks = int(input("Enter your total marks out of 600: "))
    percentage = (total_marks / 600) * 100
    print(f"Your percentage is: {percentage:.2f}%")
    #group info
    group = input("Enter your +2 group (Commerce / Computer Science / Biology / Pure Science): ").strip().lower()
    college_name = input("Which college to apply to: ")
    district = input("Enter college District: ")
    #course eligibility
    if percentage >= 50:
        degree = input("Choose your degree (Engineering / Arts and Science): ").strip().lower()
        
        # Restrict Engineering for Non-Eligible Groups
        if degree == "engineering" and group not in ["biology", "computer science"]:
            print("\n You are not eligible for Engineering. Only Biology and Computer Science students can apply.")
            print(" You can only apply for Arts & Science courses.")
            degree = "arts and science"
    else:
        print("\n Your percentage is below 50%. You are eligible only for Arts and Science courses.")
        degree = "arts and science"
    # Course selection 
    engineering_departments = [
        "Information Technology", "Computer Science", "Electrical and Electronics",
        "Electrical Communication", "Biotechnology", "Pharmaceutical",
        "Mechanical", "Civil", "Automobile"]
    arts_science_departments = [
        "BBA", "BCA", "Fashion Technology", "Catering",
        "BSc Nursing", "BA Tamil", "BA English", "BSc Maths", "Microbiology"]
    #  validate course choose
    def valid_course(department_list):
        while True:
            course_num = input("Enter the department number (1-9): ")
            if course_num.isdigit() and 1 <= int(course_num) <= 9:
                return department_list[int(course_num) - 1]
            print(" Invalid choice! Please enter a number between 1 and 9.")
    if degree == "engineering":
        print("\nChoose your Engineering Department:")
        print("1. Information Technology\n2. Computer Science\n3. Electrical and Electronics\n4. Electrical Communication")
        print("5. Biotechnology\n6. Pharmaceutical\n7. Mechanical\n8. Civil\n9. Automobile")
        course = valid_course(engineering_departments)

    else:  # Arts and Science
        print("\nChoose your Arts and Science Department:")
        print("1. BBA\n2. BCA\n3. Fashion Technology\n4. Catering\n5. BSc Nursing")
        print("6. BA Tamil\n7. BA English\n8. BSc Maths\n9. Microbiology")
        course = valid_course(arts_science_departments)
    # Display student details
    print("\n!---COLLEGE APPLICATION DETAILS---!")
    print(f"Student Name: {student_name}")
    print(f"Father's Name: {father_name}")
    print(f"Mother's Name: {mother_name}")
    print(f"Father's Occupation: {occupation1}")
    print(f"Mother's Occupation: {occupation2}")
    print(f"community: {community}")
    print(f"Annual Income: {annual_income}")
    print(f"First Graduate: {first_graduate.capitalize()}")
    print(f"Date of Birth: {date_of_birth}")
    print(f"Age: {age}")
    print(f"Mobile Number: {mobile_no}")
    print(f"Email Address: {email}")
    print(f"Total Marks: {total_marks}/600")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Group: {group.capitalize()}")
    print(f"College Name: {college_name}")
    print(f"District: {district}")
    print(f"Degree Chosen: {degree.capitalize()}")
    print(f"Department Allotted: {course}")
# dispaly allotment order details 
    print("\nWAITING FOR YOUR ALLOTMENT DETAILS:")
    print("\n Allotment order will be received after 2 days via email.")
    print(" Congratulations! You have successfully applied for the college.")
#fun calling
college_application()
