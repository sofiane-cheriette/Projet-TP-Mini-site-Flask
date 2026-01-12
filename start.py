"""
Script de lancement du Mini Catalogue de Jeux Vidéo
Gère proprement les interruptions Ctrl+C
"""
import subprocess
import sys
import os

def check_dependencies():
    """Vérifie et installe les dépendances si nécessaire"""
    try:
        import flask
        print("[OK] Dépendances déjà installées")
        return True
    except ImportError:
        print("[INFO] Installation des dépendances...")
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        if result.returncode == 0:
            print("[OK] Dépendances installées")
            return True
        else:
            print("[ERREUR] Échec de l'installation")
            return False

def main():
    print("=" * 40)
    print("   Mini Catalogue de Jeux Vidéo 🎮")
    print("=" * 40)
    print()
    
    # Vérifier Python
    print(f"[OK] Python {sys.version.split()[0]} détecté")
    
    # Vérifier/installer les dépendances
    if not check_dependencies():
        input("Appuyez sur Entrée pour quitter...")
        return
    
    print()
    print("[LANCEMENT] Serveur Flask sur http://localhost:5000")
    print("Appuyez sur Ctrl+C pour arrêter")
    print()
    
    # Lancer Flask
    os.environ["FLASK_APP"] = "app"
    
    while True:
        try:
            subprocess.run([
                sys.executable, "-m", "flask", "run", 
                "--host=0.0.0.0", "--port=5000"
            ])
            break  # Si Flask s'arrête normalement, on sort
        except KeyboardInterrupt:
            print()
            response = input("Voulez-vous vraiment arrêter ? (O/N) : ").strip().lower()
            if response in ['o', 'oui', 'y', 'yes']:
                print("Arrêt du serveur...")
                break
            else:
                print("Reprise du serveur...")
                print()

if __name__ == "__main__":
    main()
