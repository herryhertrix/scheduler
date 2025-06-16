from rocketry import Rocketry
from rocketry.conds import cron
import requests
import logging

# Logging ke stdout dan file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Gunakan zona waktu Jakarta
app = Rocketry(config={"timezone": "Asia/Jakarta"})

# @app.task(cron("0 9-20 * * *"))
@app.task(cron("* * * * *"))
def trigger_webhook():
    print("🚀 Menjalankan webhook...")
    try:
        response = requests.get(
            "http://admin.tokosusun.com/webhooks/workflows",
            timeout=10,
            verify=False
        )
        print(f"✅ Sukses: {response.status_code} - {response.text}")
        logging.info(f"Webhook sukses: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Gagal: {e}")
        logging.error(f"Webhook gagal: {e}")

if __name__ == "__main__":
    app.run()
