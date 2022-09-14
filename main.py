import random

input("Hello, I am Gato. I am a bot that takes your responses and adds them to my list of responses. The more you type, the more I learn. How is your day?\n")

responses = [
  "That's good!",
  "Meh",
  "Nah",
  "Yes",
  "French People",
  "No",
  "Have a wonderful day.",
  "STOP BEING MEAN!!!!",
  "Mashed potatoes",
  "...",
  "Bachelor's degree on whatever you just said"
]


while True:
  randomint = random.randrange(0,len(responses))
  
  message = input(f"--{responses[randomint]}\n")

  responses.append(message)