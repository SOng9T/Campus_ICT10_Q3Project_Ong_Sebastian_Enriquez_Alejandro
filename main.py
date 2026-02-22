from js import document
import random

'''def weather_update(e):
    weather = document.getElementById('input1').value.lower() # get user input and convert to lowercase for case sensitivity

    if weather == 'raining': # if statement, remember raining is case sensitive, so anything other than raining is false
        display(f'Take an umbrella!', target='output')
    else: # else statement
        display(f'Wear your sunglasses', target='output')'''

'''num1 = -1

if num1 > 0: #if statement (remember, will only process if condition is true)
    display(f'It is positive', target='output') 
else: #else statement 
    display(f'It is negative', target='output')'''


def check_eligibility(event):
    output_div = document.getElementById("output")
    output_div.innerHTML = ""
    output_div.style.display = "block"

    online_reg = document.getElementById("onlineReg").value
    medical_clearance = document.getElementById("medicalClearance").value
    grade_level = document.getElementById("gradeLevel").value
    section = document.getElementById("section").value

    if not online_reg or not medical_clearance or not grade_level:
        output_div.className = "not-eligible"
        output_div.innerHTML = """
        <h3>⚠️ Please fill in all necessary required fields!</h3>
        <ul>
            <li>Online Registration Status</li>
            <li>Medical Clearance Status</li>
            <li>Grade Level</li>
        </ul>
        """
        return

    try:
        grade_int = int(grade_level)
    except:
        grade_int = 0

    teams = ["Blue Bears", "Red Bulldogs", "Yellow Tigers", "Green Hornets"]

    if online_reg == "yes" and medical_clearance == "yes" and 7 <= grade_int <= 10:
        assigned_team = random.choice(teams)
        section_text = f" ({section})" if section else ""

        output_div.className = "eligible"
        output_div.innerHTML = f"""
        <h3> Congratulations, mate! Here's your team. lmao</h3>
        <ul>
            <li><strong>Grade:</strong> {grade_level}{section_text}</li>
            <li>Online Registration: ✅</li>
            <li>Medical Clearance: ✅</li>
        </ul>
        <div class="assigned-team">
             Assigned Team: <b>{assigned_team}</b>
        </div>
        """
        highlight_team_image(assigned_team)
    else:
        output_div.className = "not-eligible"
        missing = []
        if online_reg != "yes": missing.append("Online Registration")
        if medical_clearance != "yes": missing.append("Medical Clearance")
        if grade_int < 7 or grade_int > 10: missing.append("Grade Level (7–10 only)")

        output_div.innerHTML = (
            "<h3>❌ Not Eligible</h3><ul>" +
            "".join(f"<li>{m}</li>" for m in missing) +
            "</ul>"
        )

def reset_form(event=None):
    document.getElementById("onlineReg").value = ""
    document.getElementById("medicalClearance").value = ""
    document.getElementById("gradeLevel").value = ""
    document.getElementById("section").value = ""

    output_div = document.getElementById("output")
    output_div.innerHTML = ""
    output_div.style.display = "none"
    reset_team_images()

def highlight_team_image(team_name):
    reset_team_images()
    images = document.getElementById("teamImages").getElementsByTagName("img")
    for img in images:
        if img.alt == team_name:
            img.style.borderColor = "#3498db"
            img.style.boxShadow = "0 4px 8px rgba(52,152,219,0.5)"
            break

def reset_team_images():
    images = document.getElementById("teamImages").getElementsByTagName("img")
    for img in images:
        img.style.borderColor = "transparent"
        img.style.boxShadow = "none"