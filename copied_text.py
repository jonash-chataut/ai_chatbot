import pyautogui
import time
import pyperclip

# Give some time to switch to the right window
time.sleep(2)

# Step 1: Click on the icon
pyautogui.click(1016, 1048)
time.sleep(1)  # Wait for the application to open

# Step 2: Click and drag to select text
pyautogui.moveTo(614, 200)
pyautogui.mouseDown()
pyautogui.moveTo(1805, 915, duration=0.5)  # Drag smoothly
pyautogui.mouseUp()

# Step 3: Copy selected text
pyautogui.hotkey("ctrl", "c")
time.sleep(1)  # Wait for the clipboard to update

# Step 4: Get text from clipboard
text = pyperclip.paste()
print("Copied text:", text)
