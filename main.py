from rocketry import Rocketry
from rocketry.conds import cron
import requests
import logging
import pendulum

# Logging ke stdout dan file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = Rocketry()

# Task 1: Setiap jam
@app.task(cron("*/10 * * * *"))
def trigger_webhook():
    print("🚀 Menjalankan webhook workflows...")
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

# Task 2: Setiap menit
@app.task(cron("* * * * *"))  # Jalan tiap menit
def notify_telegram():
    now = pendulum.now("Asia/Jakarta")
    current_hour = now.hour

    if 9 <= current_hour < 20:
        print("📨 Mengirim notifikasi Telegram...")
        try:
            response = requests.get(
                "http://admin.tokosusun.com/webhooks/telegram/notify",
                timeout=10,
                verify=False
            )
            print(f"✅ Telegram sukses: {response.status_code} - {response.text}")
            logging.info(f"Telegram notify sukses: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"❌ Telegram gagal: {e}")
            logging.error(f"Telegram notify gagal: {e}")

if __name__ == "__main__":
    app.run()
