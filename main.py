from email_sender import SendMail
from joke_generator import JokeGenerator
from dotenv import load_dotenv
import os

load_dotenv()

joke_generator = JokeGenerator()
joke = joke_generator.get_joke()

to_user = os.getenv("RECEIVER_EMAIL")
SendMail.send_mail(to_user, "Here's a Funny Joke", joke)
