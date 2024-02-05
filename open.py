import openai
from fuzzywuzzy import fuzz
import json


api_key = '*************************************'


openai.api_key = api_key



data = [
    {"prompt": "UgandaEMR User Manual?", "completion": "UgandaEMR is a customization of OpenMRS for Uganda, initially starting with HIV related forms but later expanding to other areas such as Maternal and Child Health services, Tuberculosis treatment following guidelines issued by the Ministry of Health (MoH) under the Health Management Information System (HMIS) manuals."},
    {"prompt": "Minimum Computer Requirements", "completion": "Windows 7 (both 32-bit and 64-bit versions supported)! 4GB of RAM ! 5GHz duo core processor"},
    {"prompt": "Recommended Minimum Software Requirements", "completion": "Java 8 for UgandaEMR 2.0.0 and above (Java 7 for UgandaEMR 1.x - not recommended). ! Tomcat 7 3. MySQL 5. ! Mozilla Firefox 44"},
    {"prompt": r"Installation Directories and Menu Items", "completion": r"The installer creates the following directory structure: ! Main Directory - C:\Program Files\UgandaEMR ! Tomcat Directory - C:\Program Files\UgandaEMR\UgandaEMRTomcat ! Mysql Directory - C:\Program Files\MySQL\MySQL Server 5 ! TODO: Correct this ! After OpenMRS Configuration Files - C:\ApplicationData\OpenMRS TODO: Correct this."}
    #{"prompt": "", "completion": ""},
    #{"prompt": "", "completion": ""}
]

def find_closest_prompt(user_input):
    closest_prompt = None
    max_similarity = -1

    for item in data:
        similarity = fuzz.ratio(user_input, item["prompt"])
        if similarity > max_similarity:
            max_similarity = similarity
            closest_prompt = item

    return closest_prompt

def format_response(response):
    # Split the response by periods and add bullet points
    formatted_response = "\n".join([f"• {sentence.strip()}" for sentence in response.split("!")])
    return formatted_response

def chat_with_bot(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,  # Adjust the max tokens as needed
        stop=None
    )
    return response.choices[0].text.strip()

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    
    closest_prompt = find_closest_prompt(user_input)
    if closest_prompt is not None:
        formatted_response = format_response(closest_prompt['completion'])
        print(f"Bot:\n{formatted_response}")
    else:
        bot_response = chat_with_bot(user_input)
        formatted_response = format_response(bot_response)
        print(f"Bot:\n{formatted_response}")
