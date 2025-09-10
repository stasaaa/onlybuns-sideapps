import requests
import json
import random
import time

def send_rabbit_care_location(name, latitude, longitude):
    broker_url = "http://localhost:8083/queue/send/direct/rabbit-care-exchange/location.update"

    location_data = {
        "name": name,
        "latitude": latitude,
        "longitude": longitude
    }

    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(broker_url, data=json.dumps(location_data), headers=headers)
        if response.status_code == 200:
            print(f"✅ Uspešno poslata lokacija: '{name}'")
        else:
            print(f"❌ Greška pri slanju lokacije. Status kod: {response.status_code}")
            print(f"Odgovor servera: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Nije moguće povezati se sa brokerom. Proverite da li je aplikacija pokrenuta na portu 8083.")
        print(f"Greška: {e}")

def main():
    print("--- Pokretanje simulacije aplikacije za brigu o zečevima ---")
    
    locations = [
        ("Azil 'Zeka Zvonko'", 45.242, 19.845),
        ("Veterinar 'Šapice'", 45.253, 19.825),
        ("Sklonište za zečeve 'Medeno srce'", 45.260, 19.835)
    ]

    for name, lat, lon in locations:
        send_rabbit_care_location(name, lat, lon)
        time.sleep(random.randint(1, 3))
        
    print("\n--- Simulacija završena. ---")

if __name__ == "__main__":
    main()