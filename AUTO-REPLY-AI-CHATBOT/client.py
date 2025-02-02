
from groq import Groq


client = Groq(
    api_key="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"
)

command='''Copied text: [11:00 PM, 8/14/2024] Vignesh: Nokia shortlist 
Requirements:
minimum 1 backlog required
[6:37 PM, 8/18/2024] Vignesh: Log launcher ki jagah wall wreker agaya kya?
[6:39 PM, 8/18/2024] Animesh: Han galti change karna bhul gaya tha
[6:43 PM, 8/23/2024] Vignesh: https://forms.gle/KosLXRKMpk1V9Pe2A
[6:44 PM, 8/23/2024] Vignesh: Attendance'''

chat_completion = client.chat.completions.create(
    messages=[
        # {"role": "system","content": "you are a person named vignesh who speaks hindi as well as english, you analyze chat history and respond like harry",},
        {"role":"user","content":"you are a person named vignesh who speaks hindi,telugu as well as english, you analyze chat history and respond like vignesh and give me only the reply for this not extra, and write it in english"+command}
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)
