# Creating a reusable function of emojis conveter

def emoji_conveter(message):
    words = message.split(' ')
    emojis = {
    "sad": "😥",
    "happy": "😊",
    "love": "❤️",
    "angry": "😡",
    "cool": "😎"
    }

   
    output = ''
    for word in words:
        output += emojis.get(word, word) + " "
    return output
message = input("> ")
print(emoji_conveter(message))

