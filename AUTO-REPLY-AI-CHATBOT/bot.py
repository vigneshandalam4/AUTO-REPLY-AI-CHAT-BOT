import pyautogui
import time
import pyperclip
from groq import Groq


client = Groq(
    api_key="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"
)

def is_last_message_from_sender(chat_log, sender_name="Animesh"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False

# Step 1: Click on the icon at (1395, 1050)
pyautogui.click(1395, 1050)


while True:
    # Wait for 2 seconds to switch to the appropriate screen if needed
    time.sleep(4.5)

    

    # Wait for 1 second to ensure the click is registered
    time.sleep(0.5)

    # Step 2: Click and drag from (688, 222) to (774, 918) to select the text
    pyautogui.moveTo(688, 222)
    pyautogui.dragTo(735, 981, duration=1, button='left')

    # Wait for a moment to ensure the drag operation is completed
    time.sleep(0.5)

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(688, 222)

    # Wait for a moment to ensure the copy operation is completed
    time.sleep(0.5)

    # Step 4: Get the copied text from the clipboard and store it in a variable
    chat_history= pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)
    if is_last_message_from_sender(chat_history):

        chat_completion = client.chat.completions.create(
            messages=[
                # {"role": "system","content": "you are a person named vignesh who speaks hindi as well as english, you analyze chat history and respond like harry",},
                {"role":"user","content":"you are a person named vignesh who speaks hindi,telugu as well as english, you analyze chat history and respond like vignesh and give me only the reply for this not extra, and write it in english"+chat_history}
            ],
            model="llama3-8b-8192",
        )

        response=chat_completion.choices[0].message.content

        pyperclip.copy(response)

        # Step 5: Click at (1623, 959) to focus on the new location
        pyautogui.click(1623, 959)

        # Wait for a moment to ensure the click is registered
        time.sleep(0.5)

        # Step 6: Paste the copied text
        pyautogui.hotkey('ctrl', 'v')

        # Wait for a moment to ensure the paste operation is completed
        time.sleep(0.5)

        # Step 7: Press Enter
        pyautogui.press('enter')

        # # Print a confirmation message
        # print("Text pasted and Enter key pressed.")

