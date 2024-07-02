import js
from pyscript import document

def score_update(event):
    player1_score = js.document.getElementById('player1_score')
    player2_score = js.document.getElementById('player2_score')

    output_div1 = document.querySelector('#player1_score_result')
    output_div1.textContent = player1_score

    output_div2 = document.querySelector('#player2_score_result')
    output_div2.textContent = player2_score


# document.querySelector('#count').addEventListener('click', score_update)