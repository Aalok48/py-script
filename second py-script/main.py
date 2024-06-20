from pyscript import document

def counter(event):
    input_text = document.querySelector('#counter')
    sentence = input_text.value
    words = sentence.split()
    word_count = len(words)
    output_div = document.querySelector('#counter-result')
    output_div.textContent = f"Word count: {word_count}"

document.querySelector('#count').addEventListener('click', counter)