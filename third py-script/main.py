from pyscript import document

def score_update(event):
    result = 0
    player_score_ = document.queryselector('#player_score')
    print(player_score_)


    
    output_div = document.querySelector('#player_result')
    output_div.innerText = result
