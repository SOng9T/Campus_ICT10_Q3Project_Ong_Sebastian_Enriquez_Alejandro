from js import document

def display_players(event=None):
    # Clear the players list and stats
    document.getElementById("playersList").innerHTML = ""
    
    #used ai since i dont wanna arrange it alphabetically manually 
    classmates = [
        "Alejandro Enriquez",
        "Allen Daradal",
        "Bea Vilale",
        "Caleb Arias",
        "Calvin Garcia",
        "Carl Joseph Rufo",
        "Cedric Bonzon",
        "Deryck Tan",
        "Harmony Gail Yao",
        "Ivy Zosa",
        "Jalainie Abdullah",
        "Khloe Espina",
        "Leona Abeleda",
        "Martina Cajucom",
        "Miguel Sanchez",
        "Phoebe Catimbang",
        "Prince Gano",
        "Ramon Santos",
        "Renzo Arce",
        "Sean Cotioco",
        "Sebastian Ong",
        "Simrandip Kaur",
        "Skyler Escobar"
    ]
    
    #nevermind found this fire ahh variable is just a list of names, and we can use the sort() method to arrange it alphabetically without doing it manually, thanks python broiski
    classmates.sort()
    
    #to display each classmate, we can use a for loop to iterate through the list and create a card for each classmate, we can also add a random team assignment for fun (not based on actual team checker results)
    for classmate in classmates:
        #student card
        document.getElementById("playersList").innerHTML += f"""
        <div class="player-card">
            <div class="player-name"> {classmate}</div>
            <div class="player-grade">Registered for Intramurals 2025</div>
        </div>
        """
    
    # Also show total count using a WHILE LOOP (just to demonstrate both loops) - we can use a while loop to show the total number of players, we can also show how many players are in each team if we want to get fancy with it!!!
    document.getElementById("stats").innerHTML = ""
    count = 0
    total_students = len(classmates)
    
    while count < 1: #note for aj, this is just to show the total count once, we can also use it to show how many players are in each team, wanted to experiment with it 
        document.getElementById("stats").innerHTML = f"""
        <div class="stat-item">
            <div class="stat-value">{total_students}</div>
            <div class="stat-label">TOTAL PLAYERS</div>
        </div>
        """
        count += 1

# Load players when page loads
display_players()

'''from pyscript import display, document

def display_numbers(e):
    document.getElementById('result').innerHTML = " "

    count = 0

    while count < 11:
        display(count, target='result')
        count += 1

def display_numbers(e):
    document.getElementById("output").innerHTML = " "

    subjects = ["Math", "Science", "History", "English", "Filipino"]

    for subject in subjects:
        display(f'- {subject}')

'''