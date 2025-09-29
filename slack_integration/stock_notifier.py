import yfinance as yf
from slack_sdk import WebClient

# Slack setup
SLACK_TOKEN = "xoxb-XXXXXXXXXXXX"   # 🔑 Replace with your token
SLACK_CHANNEL = "ABC"  # Or channel ID like C1234567890
client = WebClient(token=SLACK_TOKEN)

def get_stock_price(symbol="SBIN.BO"):
    """Fetch stock price from Yahoo Finance"""
    stock = yf.Ticker(symbol)
    todays_data = stock.history(period="1d")
    last_quote = todays_data["Close"].iloc[-1]
    return round(last_quote, 2)

def send_slack_message(message):
    """Send message to Slack channel"""
    client.chat_postMessage(channel=SLACK_CHANNEL, text=message)

if __name__ == "__main__":
    price = get_stock_price("SBIN.BO")  # NSE/BSE stock code
    message = f"📈 SBI Stock Update: ₹{price}"
    send_slack_message(message)
    print("Message sent to Slack ✅")