import requests
import time

def receive_ad_message():
    queue_name = "ad-agency2-queue"
    broker_url = f"http://localhost:8083/queue/receive/{queue_name}"

    try:
        response = requests.get(broker_url)
        if response.status_code == 200:
            ad_message = response.json()
            if ad_message:
                print(f"✅ Agency 2 received a new ad:")
                print(f"   description: {ad_message['description']}")
                print(f"   user: {ad_message['username']}, timestamp: {ad_message['timestamp']}")
                return True
        elif response.status_code == 204:
            print("Agency 2: No new ads, waiting...")
        else:
            print(f"❌ Agency 2: Error receiving message. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Agency 2: Could not connect to broker. Error: {e}")
    return False

def main():
    print("--- Agency 2 started. Awaiting ads... ---")
    while True:
        receive_ad_message()
        time.sleep(5)  # checks every 5 secs

if __name__ == "__main__":
    main()