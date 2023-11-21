import os

bad_commit_hash = "c1a4be04b972b6c17db242fc37752ad517c29402"
good_commit_hash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"

os.system(f"git bisect start {bad_commit_hash} {good_commit_hash}")

# Commande de test
test_command = "python manage.py test"

# Exécuter git bisect avec la commande de test
os.system(f"git bisect run {test_command}")

# Réinitialiser git bisect une fois terminé
os.system("git bisect reset")
