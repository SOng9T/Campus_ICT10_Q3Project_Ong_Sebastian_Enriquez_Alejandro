from js import document
import time


def sign_up(event):
    output_div = document.getElementById("output")
    output_div.innerHTML = ""
    output_div.style.display = "block"
    
    #form values, output_div is the div where out will be displayed, after these values, it'll return here. w3schools return fields for validation check below for notes!
    fullname = document.getElementById("fullname").value
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value
    email = document.getElementById("email").value
    password = document.getElementById("password").value
    confirm_password = document.getElementById("confirm_password").value
    
    #validation page for values
    if not fullname or not grade or not section or not email or not password or not confirm_password:
        output_div.className = "error"
        output_div.innerHTML = "<h3>⚠️ Please fill in all fields!</h3>"
        return
    
    if password != confirm_password:
        output_div.className = "error"
        output_div.innerHTML = "<h3>❌ Passwords do not match!!!</h3>"
        return
    
    if len(password) < 8:
        output_div.className = "error"
        output_div.innerHTML = "<h3>❌ Password must be at least 8 characters!!!!!</h3>"
        return
    
    if "@" not in email or "." not in email or not email.endswith("@obmc.edu.ph"):
        output_div.className = "error"
        output_div.innerHTML = "<h3>❌ Please enter a valid email address! (use obmc.edu.ph as guide please)</h3>"
        return
    
    #succession of return fields
    output_div.className = "success"
    output_div.innerHTML = f"""
    <h3>✅ Account Created Successfully! Have fun playing intrams :></h3>
    <p>Welcome to Intramurals 2025, {fullname}!</p>
    <p><strong>Details:</strong></p>
    <ul>
        <li>Grade: {grade}</li>
        <li>Section: {section}</li>
        <li>Email: {email}</li>
    </ul>
    <p>Please proceed to the Team Checker page to get your team assignment!</p>
    """

def reset_form(event=None):
    document.getElementById("fullname").value = ""
    document.getElementById("grade").value = ""
    document.getElementById("section").value = ""
    document.getElementById("email").value = ""
    document.getElementById("password").value = ""
    document.getElementById("confirm_password").value = ""
    
    output_div = document.getElementById("output")
    output_div.innerHTML = ""
    output_div.style.display = "none"


    """def positive_or_negative(e):
    document.getElementById('output').innerHTML = """ 

    """num1 = int(document.getElementById('input1').value)

    if num1 > 0:
        display(f'Number {num1} is a positive', target='output')
    elif num1 == 0:
        display(f'It is zero', target='output')
    else:
        display(f'It is negative', target='output')
        
def myfunction():
  return 3+3
  print("Hello, World!")

print(myfunction())
        from pyscript import display, document
'''def account_authenticator(e): 
    document.getElementById("output").innerHTML = " "

    username = document.getElementById("name").value
    digits = document.getElementById("digits").value

    if username.isalpha():
        if digits.isdigit() and len(digits) == 4:
            document.getElementById("output").innerHTML = f"Welcome, {username}! Your digit is {digits}."
        else:
            document.getElementById("output").innerHTML = "Invalid!"
    else:
        document.getElementById("output").innerHTML = "Invalid username. Please use only letters."'''
def account_authenticator(e):

    document.getElementById("output").innerHTML = " "

    username = document.getElementById("name").value
    password = document.getElementById("digits").value

    #7 characters username
    if len(username) >= 7:

        # Password checks
        has_letter = any(char.isalpha() for char in password)
        has_number = any(char.isdigit() for char in password)

        #for 10 characters
        if len(password) >= 10:

            # Password will contain at least one letter and one number for mr ortiz
            if has_letter and has_number:
                document.getElementById("output").innerHTML = f"Welcome, {username}! Account created successfully homie :>"
            else:
                document.getElementById("output").innerHTML = "Password must contain at least one letter and one number."

        else:
            document.getElementById("output").innerHTML = "passwordd must be at least 10 characters long."

    else:
        document.getElementById("output").innerHTML = "username must be at least 7 characters long please"

        """
