from bardapi import Bard
from dotenv import load_dotenv

load_dotenv()

def call_bard(query):
   bard = Bard()
   answer = bard.get_answer(query)
   return (answer['content'])
