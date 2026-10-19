# Set Operators
from pyscript import display, document

def club_member(e):

    document.getElementById('result').innerHTML = ' '
    first_name = document.getElementById('firstname').value.lower().strip()
    last_name = document.getElementById('lastname').value.lower().strip()
    name = first_name + ' ' + last_name
    club_members = ["mj arbison", "basty uclaray", "cody deocampo", "bonnie nubla", "alexa agnote", "aisha padua",'eric levring']
    club_checker = name in club_members
    display_message = (f'Sorry, there is no {name} in club', f'{name} is in the club')
    display(display_message[club_checker], target='result')
    

    grade_seven = {'mj arbison', 'cody deocampo'} 
    grade_eight = {'keane pacana', 'bonnie nubla'}
    grade_nine = {'alexa agnote', 'aisha padua'}
    grade_ten = {'eric levring', 'basty uclaray'}
    total_member = {"mj arbison", "basty uclaray", "cody deocampo", "bonnie nubla", "alexa agnote", "aisha padua","eric levring"}

    display(grade_seven | grade_eight | grade_nine | grade_ten, target='result')
    display(f'Total number of members: {len(total_member)}', target='result')
