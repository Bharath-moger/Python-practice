    # from slack_bolt import App
    # from slack_bolt.adapter.socket_mode import SocketModeHandler

    # # Replace with your tokens
    # SLACK_BOT_TOKEN = "xoxb"   # Bot User OAuth Token
    # SLACK_APP_TOKEN = "xapp"   # App-Level Token with connections:write

    # # Initialize Slack app
    # app = App(token=SLACK_BOT_TOKEN)

    # # Listen to all message events
    # @app.event("message")
    # def handle_message_events(body, logger):
    #     event = body.get("event", {})
    #     user = event.get("user")
    #     text = event.get("text")
    #     channel = event.get("channel")

    #     # Ignore messages from bots
    #     if user and text:
    #         print(f"💬 New message in channel {channel} from {user}: {text}")

    # if __name__ == "__main__":
    #     print("🚀 Listening for Slack messages...")
    #     handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    #     handler.start()

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Tokens
SLACK_BOT_TOKEN = "xoxb-AAAAAAAAAAAA"   # Bot User OAuth Token
SLACK_APP_TOKEN = "xapp-1-AAAAAAAAAAAAAAAAAAAAAAAAAA"   # App-Level Token with connections:write

# Initialize app
app = App(token=SLACK_BOT_TOKEN)

# --- Helper functions ---
def get_channel_name(client, channel_id):
    try:
        info = client.conversations_info(channel=channel_id)
        return info["channel"]["name"]
    except Exception:
        return channel_id  # fallback to ID

def get_user_name(client, user_id):
    try:
        info = client.users_info(user=user_id)
        return info["user"]["real_name"]  # or "name" for username
    except Exception:
        return user_id  # fallback to ID

# --- Event handler ---
@app.event("message")
def handle_message_events(body, say, client):
    event = body.get("event", {})
    user_id = event.get("user")
    text = event.get("text")
    channel_id = event.get("channel")

    if user_id and text:
        channel_name = get_channel_name(client, channel_id)
        user_name = get_user_name(client, user_id)
        print(f"💬 New message in #{channel_name} from {user_name}: {text}")

# --- Start app ---
if __name__ == "__main__":
    print("🚀 Listening for Slack messages...")
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
