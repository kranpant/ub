import time
import asyncio
from aiohttp import ClientSession
from SHUKLAUSER.Helpers import app, github

__Version__ = "1.0.0"

boot = time.time()

app = app
one = one
two = two
three = three
four = four
five = five

github()

# Create a placeholder session
aiohttpsession = None

# Function to initialize it later
async def get_session():
    global aiohttpsession
    if aiohttpsession is None or aiohttpsession.closed:
        aiohttpsession = ClientSession()
    return aiohttpsession
  
