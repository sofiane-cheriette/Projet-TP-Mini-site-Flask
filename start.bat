@echo off
setlocal

:: Ignorer Ctrl+C pour eviter l'arret accidentel
break off

echo ========================================
echo    Mini Catalogue de Jeux Video
echo ========================================
echo.

:: Verifier si Python est installe
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] Python n'est pas installe !
    echo Telechargez-le sur : https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python detecte

:: Verifier si les dependances sont installees
python -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo [INFO] Installation des dependances...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERREUR] Echec de l'installation des dependances
        pause
        exit /b 1
    )
    echo [OK] Dependances installees
) else (
    echo [OK] Dependances deja installees
)

echo.
echo [LANCEMENT] Serveur Flask sur http://localhost:5000
echo Appuyez sur Ctrl+C pour arreter
echo.

python -m flask run --host=0.0.0.0 --port=5000
