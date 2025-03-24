import tkinter as tk
from tkinter import messagebox

def college_application():
    # Create a new Tkinter window
    root = tk.Tk()
    root.title("College Application Form")

    # Function to handle form submission
    def submit_form():
        # Retrieving the values entered in the form fields
        student_name = student_name_entry.get()
        father_name = father_name_entry.get()
        mother_name = mother_name_entry.get()
        occupation1 = occupation1_entry.get()
        occupation2 = occupation2_entry.get()
        community = community_entry.get()
        annual_income = int(annual_income_entry.get())
        first_graduate = first_graduate_var.get()
        date_of_birth = dob_entry.get()
        age = int(age_entry.get())
        mobile_no = mobile_no_entry.get()
        email = email_entry.get()
        total_marks = int(total_marks_entry.get())
        group = group_var.get()
        college_name = college_name_entry.get()
        district = district_entry.get()

        # Calculating the percentage
        percentage = (total_marks / 600) * 100

        # Determine degree eligibility
        degree = degree_var.get()
        if percentage < 50:
            degree = "Arts and Science"

        # Display results in messagebox
        messagebox.showinfo("Application Submitted", f"""
        Student Name: {student_name}
        Father's Name: {father_name}
        Mother's Name: {mother_name}
        Father's Occupation: {occupation1}
        Mother's Occupation: {occupation2}
        Community: {community}
        Annual Income: {annual_income}
        First Graduate: {first_graduate}
        Date of Birth: {date_of_birth}
        Age: {age}
        Mobile No: {mobile_no}
        Email: {email}
        Total Marks: {total_marks}/600
        Percentage: {percentage:.2f}%
        Group: {group}
        College Name: {college_name}
        District: {district}
        Degree: {degree}
        """)

        # For scholarship eligibility
        if first_graduate.lower() == "yes":
            messagebox.showinfo("Scholarship", "You are eligible for a scholarship, and the total fees will be reduced by a certain amount!")
        else:
            messagebox.showinfo("Scholarship", "You are not a first graduate, so no scholarship is available.")

        # Display final message
        messagebox.showinfo("College Application", "Congratulations! You have successfully applied for the college. Waiting for allotment details.")

    # Create the Tkinter widgets for the form fields
    tk.Label(root, text="Student Name:").grid(row=0, column=0)
    student_name_entry = tk.Entry(root)
    student_name_entry.grid(row=0, column=1)

    tk.Label(root, text="Father's Name:").grid(row=1, column=0)
    father_name_entry = tk.Entry(root)
    father_name_entry.grid(row=1, column=1)

    tk.Label(root, text="Mother's Name:").grid(row=2, column=0)
    mother_name_entry = tk.Entry(root)
    mother_name_entry.grid(row=2, column=1)

    tk.Label(root, text="Father's Occupation:").grid(row=3, column=0)
    occupation1_entry = tk.Entry(root)
    occupation1_entry.grid(row=3, column=1)

    tk.Label(root, text="Mother's Occupation:").grid(row=4, column=0)
    occupation2_entry = tk.Entry(root)
    occupation2_entry.grid(row=4, column=1)

    tk.Label(root, text="Community:").grid(row=5, column=0)
    community_entry = tk.Entry(root)
    community_entry.grid(row=5, column=1)

    tk.Label(root, text="Annual Income:").grid(row=6, column=0)
    annual_income_entry = tk.Entry(root)
    annual_income_entry.grid(row=6, column=1)

    tk.Label(root, text="Are you the first graduate in the family? (yes/no):").grid(row=7, column=0)
    first_graduate_var = tk.StringVar()
    first_graduate_entry = tk.Entry(root, textvariable=first_graduate_var)
    first_graduate_entry.grid(row=7, column=1)

    tk.Label(root, text="Date of Birth (DD/MM/YYYY):").grid(row=8, column=0)
    dob_entry = tk.Entry(root)
    dob_entry.grid(row=8, column=1)

    tk.Label(root, text="Age:").grid(row=9, column=0)
    age_entry = tk.Entry(root)
    age_entry.grid(row=9, column=1)

    tk.Label(root, text="Mobile Number:").grid(row=10, column=0)
    mobile_no_entry = tk.Entry(root)
    mobile_no_entry.grid(row=10, column=1)

    tk.Label(root, text="Email Address:").grid(row=11, column=0)
    email_entry = tk.Entry(root)
    email_entry.grid(row=11, column=1)

    tk.Label(root, text="Total Marks (out of 600):").grid(row=12, column=0)
    total_marks_entry = tk.Entry(root)
    total_marks_entry.grid(row=12, column=1)

    tk.Label(root, text="+2 Group (Commerce / Computer Science / Biology / Pure Science):").grid(row=13, column=0)
    group_var = tk.StringVar()
    group_entry = tk.Entry(root, textvariable=group_var)
    group_entry.grid(row=13, column=1)

    tk.Label(root, text="College Name:").grid(row=14, column=0)
    college_name_entry = tk.Entry(root)
    college_name_entry.grid(row=14, column=1)

    tk.Label(root, text="District:").grid(row=15, column=0)
    district_entry = tk.Entry(root)
    district_entry.grid(row=15, column=1)

    tk.Label(root, text="Choose Degree (Engineering / Arts and Science):").grid(row=16, column=0)
    degree_var = tk.StringVar()
    degree_entry = tk.Entry(root, textvariable=degree_var)
    degree_entry.grid(row=16, column=1)

    # Submit Button
    submit_button = tk.Button(root, text="Submit Application", command=submit_form)
    submit_button.grid(row=17, columnspan=2)

    # Start the Tkinter main loop
    root.mainloop()

# Call the function to run the Tkinter app
college_application()
