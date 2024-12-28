
random_text = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
    'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)
new_text = []

for text in random_text.split():
    punctuation = ''
    if text.endswith(','):
        punctuation = ','
        text = text[:-1]
    elif text.endswith('.'):
        punctuation = '.'
        text = text[:-1]

    new_text.append(text + 'ing' + punctuation)

new_text_string = ' '.join(new_text)
print(new_text_string)
