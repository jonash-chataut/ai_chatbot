import pyautogui
import time
import pyperclip
from openai import OpenAI
import re
import google.generativeai as genai

# Set up your API key
genai.configure(api_key="AIzaSyDJpW9h_UIh7xYPOnki-2GAY0mLn6xGcWQ")

# Load the model
model = genai.GenerativeModel("gemini-2.0-flash") 


# function to see if the last message is from responder or not

def is_last_message_from_user(chat_history, username, botname="You"):
    # Split lines, strip empty ones
    lines = [line.strip() for line in chat_history.strip().split("\n") if line.strip()]

    sender = None

    i = 0
    while i < len(lines):
        line = lines[i]

        # Skip timestamp lines
        if is_timestamp(line):
            i += 1
            continue

        # If this line is a sender name
        sender = line

        # Next line should be the message (skip)
        i += 2  # move to next sender

    # After loop: "sender" contains the last message sender
    if sender == username:
        return True
    elif sender == botname:
        return False
    else:
        return False

def is_timestamp(line):
    return bool(re.match(r'^\d{1,2}:\d{2}$', line))




# Give some time to switch to the right window
time.sleep(2)

 # Step 1: Click on the icon
pyautogui.click(1046, 1048)
time.sleep(2)  # Wait for the application to open

# for knowing the username of the responder
pyautogui.moveTo(678, 130)
pyautogui.mouseDown()
pyautogui.moveTo(804, 144, duration=0.5)  # Drag smoothly
pyautogui.mouseUp()

# Copy selected text
pyautogui.hotkey("ctrl", "c")
time.sleep(1)  # Wait for clipboard update

# Get copied text from clipboard
# username = pyperclip.paste()
# print(username)
username = "cricphobia_17"
# Click at (840, 969)
pyautogui.click(840, 969)
time.sleep(1)
try:
    while True:

     
       # Step 2: Click and drag to select text
        pyautogui.moveTo(1850, 200)
        pyautogui.mouseDown()
        pyautogui.moveTo(1850, 900, duration=1.5)  # Drag smoothly
        pyautogui.mouseUp()

        # Step 3: Copy selected text
        pyautogui.hotkey("ctrl", "c")
        time.sleep(1)  # Wait for the clipboard to update
        pyautogui.click(1048, 141)

        # Step 4: Get text from clipboard
        chat = pyperclip.paste()
        print("Copied text:", chat)
        if is_last_message_from_user(chat,username):
            try:
                # chat response
                # prompt = f"""
                #         You are a person named 'You' and will be referred to as 'You' in the text. You are from Nepal and work as a coder. You communicate naturally, responding in the same language as the other person. If the other person uses Nepali or Hindi, you will reply in that language. Only reply in the language that the other person uses. Your replies should be short, sweet, and engaging, just like a real person would respond. You adapt to the mood and tone of the conversation, always keeping it light and casual, and avoid long-winded responses. Ensure that you are responding only to the actual message content from the user and not to labels or metadata (like "You sent" or "cricphobia_17"). Ignore any labels when generating your response and focus solely on the content of the conversation.

                #         User: {chat}
                #         """

                # Generate response
                # response = model.generate_content(prompt)
                 # Generate response (better way: use messages[])
                response = model.generate_content(messages=[
                    {"role": "system", "content": """
                    You are a person named 'You' and will be referred to as 'You' in the text. You are from Nepal and work as a coder. You communicate naturally, responding in the same language as the other person. If the other person uses Nepali or Hindi, you will reply in that language. Only reply in the language that the other person uses. Your replies should be short, sweet, and engaging, just like a real person would respond. You adapt to the mood and tone of the conversation, always keeping it light and casual, and avoid long-winded responses. Ensure that you are responding only to the actual message content from the user and not to labels or metadata (like 'You sent' or 'cricphobia_17'). Ignore any labels when generating your response and focus solely on the content of the conversation.
                    """},
                    {"role": "user", "content": chat}
                ])

                # Print response
                # print("Bot:", response.text)
                # Step 5: Click at (840, 969)
                pyautogui.click(840, 969)
                time.sleep(1)

                # Step 6: Paste the copied text
                pyperclip.copy(response.text)
                pyautogui.hotkey("ctrl", "v")
                time.sleep(1)
                # Step 7: Press Enter
                pyautogui.press("enter")
                # wait for 30 second after sending reply
                time.sleep(30)
            except Exception as e:
                print(e)
        else:
            time.sleep(60)
except KeyboardInterrupt:
    print("\nBot stopped manually with Ctrl+C.")

except Exception as e:
    print("Fatal error occurred:", e)

finally:
    print("Bot exited. Goodbye!")

