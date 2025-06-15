from rocketry import Rocketry
from rocketry.conds import cron
import requests
import logging

# Logging ke stdout dan file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = Rocketry()

@app.task(cron("0 9-20 * * *"))
def trigger_webhook():
    print("🚀 Menjalankan webhook...")
    try:
        response = requests.get("https://admin.tokosusun.com/webhooks/workflows", timeout=10)
        print(f"✅ Sukses: {response.status_code} - {response.text}")
        logging.info(f"Webhook sukses: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Gagal: {e}")
        logging.error(f"Webhook gagal: {e}")

if __name__ == "__main__":
    app.run()