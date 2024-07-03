import js
from pyscript import document

def score_update(event):
    # Get the selected radio button for player 1
    player1_selected = js.document.querySelector('#player1_score input[name="run"]:checked')
    player1_score = int(player1_selected.value)  # Convert to integer

    # Get the selected radio button for player 2
    player2_selected = js.document.querySelector('#player2_score input[name="run"]:checked')
    player2_score = int(player2_selected.value)  # Convert to integer

    # Update the score display
    output_div1 = document.querySelector('#player_result')
    output_div1.textContent = f"Alok karn: {player1_score}"

    output_div2 = document.querySelector('#player_result')
    output_div2.textContent = f"Subhash Mandal: {player2_score}"
