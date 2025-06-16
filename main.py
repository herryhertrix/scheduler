from rocketry import Rocketry
from rocketry.conds import cron
import requests
import logging
import urllib3

# Matikan warning SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Rocketry dengan zona waktu & eksekusi eksplisit
app = Rocketry(config={"timezone": "Asia/Jakarta"}, task_execution="async")

@app.task(cron("0 9-20 * * *"))
def trigger_webhook():
    print("🚀 Menjalankan webhook...")
    try:
        response = requests.get(
            "http://admin.tokosusun.com/webhooks/workflows",
            timeout=10,
            verify=False  # self-signed SSL accepted
        )
        print(f"✅ Sukses: {response.status_code} - {response.text}")
        logging.info(f"Webhook sukses: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Gagal: {e}")
        logging.error(f"Webhook gagal: {e}")

if __name__ == "__main__":
    app.run()
