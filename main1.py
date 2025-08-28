import pyautogui
import time
import pyperclip
from openai import OpenAI
import re
# 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
# ai for chat response
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key= "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"
    )

# function to see if the last message is from responder or not
def is_last_message_from_user(chat_history, username):
    lines = chat_history.strip().split("\n") #list ma converting
    if len(lines) < 2:
        return False  # No second last line, so can't check
    second_last_message=lines[-2] #second last line accessing
    if username in second_last_message:
        return True
    return False


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
username = pyperclip.paste()

# Click at (840, 969)
pyautogui.click(840, 969)
time.sleep(1)

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
            completion = client.chat.completions.create(
                model="google/gemini-2.0-flash-thinking-exp:free",
                messages=[
                    {"role": "system", "content": """
                     You are a person named 'You' and will be referred to as 'You' in the text. You are from Nepal and work as a coder. You communicate naturally, responding in the same language as the other person. If the other person uses Nepali or Hindi, you will reply in that language. Only reply in the language that the other person uses. Your replies should be short, sweet, and engaging, just like a real person would respond. You adapt to the mood and tone of the conversation, always keeping it light and casual, and avoid long-winded responses. Ensure that you are responding only to the actual message content from the user and not to labels or metadata (like "You sent" or "cricphobia_17"). Ignore any labels when generating your response and focus solely on the content of the conversation.
                     """},
                    {
                        "role": "user",
                        "content": chat
                    }
                ]
            )
            reply=completion.choices[0].message.content
            # reply = response.choices[0].message['content']


            # Step 5: Click at (840, 969)
            pyautogui.click(840, 969)
            time.sleep(1)

            # Step 6: Paste the copied text
            pyperclip.copy(reply)
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

