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
    now = pendulum.now("Asia/Jakarta")
    current_hour = now.hour
    
    if 9 <= current_hour <= 21:
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

    if 9 <= current_hour <= 21:
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

    # Tambahan: Withdraw jam 01:00 dan Inventory jam 06:00
    if current_hour == 1:
        print("🏦 Menjalankan withdraw workflows (01:00)...")
        try:
            response = requests.get(
                "http://admin.tokosusun.com/webhooks/workflows/withdraw",
                timeout=10,
                verify=False
            )
            print(f"✅ Withdraw sukses: {response.status_code} - {response.text}")
            logging.info(f"Withdraw sukses: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"❌ Withdraw gagal: {e}")
            logging.error(f"Withdraw gagal: {e}")
    elif current_hour == 6:
        print("📦 Menjalankan inventory workflows (06:00)...")
        try:
            response = requests.get(
                "http://admin.tokosusun.com/webhooks/workflows/inventory",
                timeout=10,
                verify=False
            )
            print(f"✅ Inventory sukses: {response.status_code} - {response.text}")
            logging.info(f"Inventory sukses: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"❌ Inventory gagal: {e}")
            logging.error(f"Inventory gagal: {e}")

if __name__ == "__main__":
    app.run()
