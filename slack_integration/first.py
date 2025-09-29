from slack_sdk import WebClient

# paste your bot token here
slack_token = "xoxb-XXXXXXXXXXXXXXXXX"
client = WebClient(token=slack_token)

client.chat_postMessage(
    channel="ABC",   # change to your channel
    text="Hello! 👋 This is a test message from Python."
)
print("message sent to you channel ")