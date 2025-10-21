# Emoji converter using dictionaries (loop version)

emojis = {
    "sad": "😥",
    "happy": "😊",
    "love": "❤️",
    "angry": "😡",
    "cool": "😎"
}

while True:
    message = input("> ")

    if message.lower() == "quit":
        break

    words = message.split(' ')
    output = ''
    for word in words:
        output += emojis.get(word, word) + " "

    print(output)
