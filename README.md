# 20250617-test-application-en-ligne
Choisir un hébergeur gratuit/simple, Créer un compte Railway et déployer
Le plus simple aujourd’hui est d’utiliser Railway (rapide, inscription avec Google possible, interface intuitive).
Tu peux aussi utiliser Render ou PythonAnywhere si tu préfères, mais Railway est parfait pour ce genre de mini API.
1. Va sur https://railway.app/
•	Clique sur Sign in (connexion avec Google possible)
•	Clique sur New Project > Deploy from GitHub repo ou Start from Template
2. Upload ton projet
•	Pour Railway, le plus simple est de créer un dépôt GitHub avec tes 4 fichiers, puis de le connecter à Railway.
•	Ou tu peux utiliser le bouton "Start from Blank", puis Upload tes fichiers dans l’interface Railway (dans “Files”).
3. Configurer le service
•	Par défaut, Railway détecte requirements.txt et lance une commande.
•	Change la commande de démarrage en :
nginx
CopierModifier
python api.py
•	Sur l’interface, va dans "Deployments" puis vérifie qu’il n’y a pas d’erreur (logs visibles sur Railway).
4. Récupérer l’URL publique
•	Une fois le projet lancé (ça prend 1-2 minutes la première fois), Railway te fournit une URL publique (exemple : https://my-churn-api.up.railway.app)
•	Teste l’API : tu peux envoyer une requête POST à https://xxx.railway.app/predict avec un outil comme Postman ou un simple script Python.
________________________________________
