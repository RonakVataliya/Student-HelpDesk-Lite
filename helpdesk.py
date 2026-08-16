def classify_message(message):
    categories = ["technical_issue", "grading_dispute", "enrollment_request", "general_question"]
    
    if "error" in message or "login" in message or "upload" in message or "website" in message or "password" in message:
        return categories[0]
    elif "grade" in message or "marks" in message or "score" in message or "assignment" in message or "incorrect" in message:
        return categories[1]
    elif "enroll" in message or "registration" in message or "course" in message or "section" in message or "add" in message or "drop" in message:
        return categories[2]
    else:
        return categories[3]

def generate_response(category):
    if category == "technical_issue":
            print("Response:\nIt looks like you have a technical issue. Please check your device, browser, and any error message.")
    elif category == "grading_dispute":
        print("Response:\nIt looks like you have a grading concern. Please provide the course and assessment details so the instructor can review it.")
    elif category == "enrollment_request":
        print("Response:\nIt looks like you have an enrollment request. Please provide the course and section details.")
    else:
        print("Response:\nPlease provide more details about your question so I can help.")

name = input("Enter you name: ")
course = input("Enter your course: ")
message = input("Enter your message: ")
checking_message = message.lower()

category = classify_message(checking_message)

Student_HelpDesk =f"""
================================
Student Helpdesk
================================

Name: {name}
Course: {course}

Message:
{message}

Category:
{category}
"""
print(Student_HelpDesk)
generate_response(category)