import time
import random
import logging

# Configuration du fichier de logs
logging.basicConfig(filename='app.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def generate_traffic():
    while True:
        # 90% du temps : Trafic normal
        if random.random() < 0.9:
            status = 200
            response_time = random.uniform(0.1, 0.5)
            logging.info(f"Status: {status}, ResponseTime: {response_time:.2f}s, IP: 192.168.1.{random.randint(1,50)}")
            print(f"✅ Requete OK - Temps: {response_time:.2f}s")
        
        # 10% du temps : Anomalie (Attaque ou Bug)
        else:
            status = random.choice([404, 500])
            response_time = random.uniform(2.0, 5.0)
            logging.error(f"Status: {status}, ResponseTime: {response_time:.2f}s, IP: 10.0.0.{random.randint(1,10)}")
            print(f"⚠️ ANOMALIE DETECTEE - Status: {status} - Temps: {response_time:.2f}s")
            
        time.sleep(2) # Attendre 2 secondes entre chaque requête

if __name__ == "__main__":
    print("🚀 Démarrage de l'application...")
    generate_traffic()
