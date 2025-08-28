import re

def is_last_message_from_user(chat_history, username):
    messages = chat_history.strip().split("\n")
    last_message = messages[-2] 
    if username in last_message:
        return True
    return False

# Example chat history stored as a string
chat_history = """
23:50
cricphobia_17
Hello
cricphobia_17
How are you
00:16
You sent
Hey there! 
I'm doing great, thanks for asking! How about you?
00:33
cricphobia_17
I also doing great
cricphobia_17
Ramro

"""

# Check if the last message is from 'cricphobia_17'
result = is_last_message_from_user(chat_history, 'cricphobia_17')
print(result)  # Output will be True, since the last message is from 'cricphobia_17'
