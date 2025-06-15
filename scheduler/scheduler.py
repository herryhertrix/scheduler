from rocketry import Rocketry
from rocketry.conds import cron
import requests

app = Rocketry()

@app.task(cron("0 9-20 * * *"))
def trigger_webhook():
    url = "https://admin.tokosusun.com/webhooks/workflows"
    try:
        response = requests.get(url, timeout=10)
        print(f"[{response.status_code}] Webhook success: {response.text}")
    except Exception as e:
        print(f"Webhook failed: {e}")

if __name__ == "__main__":
    app.run()
