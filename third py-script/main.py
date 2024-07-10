from pyscript import document

def score_update(event):
    result = 0
    player_score_div = document.querySelector('#player_score')  # Select the div

    # Get all radio buttons within the div
    radio_buttons = player_score_div.querySelectorAll('input[type="radio"]')

    # Iterate through radio buttons
    for button in radio_buttons:
        if button.checked:  # Check if the button is selected
            result += int(button.value)  # Add the value to the result

    # Update the output div
    output_div = document.querySelector('#player_result')
    output_div.innerText = result
