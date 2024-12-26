
random_text = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
    'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)
new_text = []

for text in random_text.split():
    if text.endswith(','):
        new_text.append(text[:-1] + 'ing')
    elif text.endswith('.'):
        new_text.append(text[:-1] + 'ing')
    else:
        new_text.append(text + 'ing')

new_text_string = ' '.join(new_text)
print(new_text_string)
