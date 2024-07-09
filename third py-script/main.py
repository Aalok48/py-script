from pyscript import document

def score_update(event):
    result = 0
    player_score_ = document.queryselector('#player_score')


    
    output_div = document.querySelector('#player_result')
    output_div.innerText = result
