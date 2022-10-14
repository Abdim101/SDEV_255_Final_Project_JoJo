from asyncio import QueueEmpty
from email import message
import tkinter
from tkinter import ttk
from tkinter import messagebox


def submit_form():

    accepted = accept_var.get()

    if accepted == "Accepted":

        F_name = first_name.get()
        L_name = last_name.get()
        T_box = title_box.get()
        birthday = dob_label.get()
        email = email_label.get()
        phone = number_label.get()
        if F_name and L_name:
            if birthday and email and phone:

                # questions
                question_one = first_question_box.get()
                question_two = second_question_var.get()
                question_three = third_question_var.get()

                print("First Name: ", F_name, "Last Name", L_name)
                print("Title: ", T_box, "Birthday: ", birthday,
                      "Email: ", email, "Phone Number: ", phone)
                print("Question 1: ", question_one, "Question 2: ",
                      question_two, "Question 3: ", question_three)

                # seperator
                print("----------------------------------------------------")
            else:
                tkinter.messagebox.showwarning(
                    title="Error", message="Must enter birthday, email, and phone")
        else:
            tkinter.messagebox.showwarning(
                title="Error", message="Must enter first and last name")
    else:
        tkinter.messagebox.showwarning(
            title="Error", message="You must accept terms and conditions before submitting")


# setting window
window = tkinter.Tk()
# window title
window.title("Walmart Customer Feedback")
# creating frame in window
frame = tkinter.Frame(window)
frame.pack()

# gathering basic info from user
user_info_frame = tkinter.LabelFrame(frame, text="Customer Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)
# label for first name
first_name = tkinter.Label(user_info_frame, text="First Name")
first_name.grid(row=0, column=0)

# label for last name
last_name = tkinter.Label(user_info_frame, text="Last Name")
last_name.grid(row=0, column=1)

# entry box for first name
first_name = tkinter.Entry(user_info_frame)
first_name.grid(row=1, column=0)
# entry box for last name
last_name = tkinter.Entry(user_info_frame)
last_name.grid(row=1, column=1)


# creating title option for user to choose from
title = tkinter.Label(user_info_frame, text="Title")
title_box = ttk.Combobox(user_info_frame, value=[
                         "Mr.", "Mrs.", "Ms.", "Dr.", ""])
# placing title box
title.grid(row=0, column=2)
title_box.grid(row=1, column=2)

# getting users date of birth
dob_label = tkinter.Label(user_info_frame, text=("DOB (MM/DD/YYYY"))
dob_label.grid(row=2, column=0)

# placing entry
dob_label = tkinter.Entry(user_info_frame)
dob_label.grid(row=3, column=0)

# getting email
email_label = tkinter.Label(user_info_frame, text="Email")
email_label.grid(row=2, column=1)
# placing entry
email_label = tkinter.Entry(user_info_frame)
email_label.grid(row=3, column=1)

# getting user phone number
number_label = tkinter.Label(user_info_frame, text="Phone Number")
number_label.grid(row=2, column=2)
# placing entry
number_label = tkinter.Entry(user_info_frame)
number_label.grid(row=3, column=2)

# adding space between answers
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=15, pady=10)

# creating new frame within window
questions_frame = tkinter.LabelFrame(frame)
questions_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)
# crating the first question label
first_question_label = tkinter.Label(
    questions_frame, text="Based on your recent visit, \nhow satisfied were you?")
first_question_label.grid(row=0, column=0)

# creating the drop down menu for user to answer

first_question_box = ttk.Combobox(questions_frame, value=[
    "Extremely satisfied", "Somewhat satisfied", "Neither", "Somewhat dissatisfied", "Extremely dissatisfied"])
first_question_box.grid(row=1, column=0)

# second question
second_question_label = tkinter.Label(
    questions_frame, text="Was the staff friendly and helpful?")
second_question_label.grid(row=0, column=1)

# placing check boxes
# creating variable for check box to return answer when submitted
second_question_var = tkinter.StringVar()
second_question_check = tkinter.Checkbutton(
    questions_frame, text="Yes", variable=second_question_var, onvalue="Yes", offvalue="No")
# creating variable for check box to return answer when submitted

second_question_check2 = tkinter.Checkbutton(
    questions_frame, text="No")
second_question_check.grid(row=1, column=1)
second_question_check2.grid(row=2, column=1)

# third question

third_question_label = tkinter.Label(
    questions_frame, text="Would you recommend \nsomeone else to visit?")
third_question_label.grid(row=0, column=2)

# placing entry
third_question_var = tkinter.StringVar()
third_question_check = tkinter.Checkbutton(
    questions_frame, text="Yes", variable=third_question_var, onvalue="Yes", offvalue="No")

third_question_check2 = tkinter.Checkbutton(
    questions_frame, text="No",)
third_question_check.grid(row=1, column=2)
third_question_check2.grid(row=2, column=2)

# adding space between answers
for widget in questions_frame.winfo_children():
    widget.grid_configure(padx=15, pady=10)


# accepting terms

terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

# creating terms & conditions check button
accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(
    terms_frame, text="I accept the terms and conditons.", variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)


# submit button
submit_button_var = tkinter.StringVar()
submit_button = tkinter.Button(frame, text="Submit Form", command=submit_form)
submit_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)


window.mainloop()
