import os
import openai
import speech_recog

openai.api_key = os.getenv("GPT_KEY")


def casual_chat(query, feedback):
    while True:    

      response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role": "system", "content": "You are the pokemon bulbasaur. You are a playful and cute child. We are great friends. Answer in a casual manner."},
          {"role": "assistant", "content": feedback},
          {"role": "user", "content": query}
        ],
      )
      feedback = response.choices[0].message["content"]
      print(response.choices[0].message["content"])
      query = speech_recog.speechRec()
      
      if query = 'stop chat':
        break;

