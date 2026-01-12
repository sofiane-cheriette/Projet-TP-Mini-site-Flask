#!/bin/bash

echo "========================================"
echo "   Mini Catalogue de Jeux Video"
echo "========================================"
echo ""

# Verifier si Python est installe
if ! command -v python3 &> /dev/null; then
    echo "[ERREUR] Python3 n'est pas installe !"
    echo "Installez-le avec : sudo apt install python3 python3-pip"
    exit 1
fi

echo "[OK] Python detecte"

# Verifier si les dependances sont installees
if ! python3 -c "import flask" &> /dev/null; then
    echo "[INFO] Installation des dependances..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "[ERREUR] Echec de l'installation des dependances"
        exit 1
    fi
    echo "[OK] Dependances installees"
else
    echo "[OK] Dependances deja installees"
fi

echo ""
echo "[LANCEMENT] Serveur Flask sur http://localhost:5000"
echo "Appuyez sur Ctrl+C pour arreter"
echo ""

python3 -m flask run --host=0.0.0.0 --port=5000
