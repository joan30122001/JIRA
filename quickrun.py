import argparse, os, sys, subprocess

BASE = os.path.dirname(os.path.abspath(__file__))
MANAGE = os.path.join(BASE, "manage.py")
REQ = os.path.join(BASE, "requirements.txt")

def run_list(argv, env=None):
    print("$", " ".join(argv))
    p = subprocess.run(argv, env=env)
    if p.returncode != 0:
        sys.exit(p.returncode)

def pip_install():
    if os.path.isfile(REQ):
        run_list([sys.executable, "-m", "pip", "install", "-r", REQ])
    else:
        print("requirements.txt introuvable, étape ignorée.")

def maybe_set_settings(settings):
    if settings:
        os.environ["DJANGO_SETTINGS_MODULE"] = settings

def make_superuser(email, password):
    if not email or not password:
        return
    code = f"""
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv('DJANGO_SETTINGS_MODULE',''))
django.setup()
from django.contrib.auth import get_user_model
U = get_user_model()
user = U.objects.filter(email='{email}').first() or U.objects.filter(username='{email}').first()
if not user:
    try:
        U.objects.create_superuser(username='{email}', email='{email}', password='{password}')
        print('Superuser créé: {email}')
    except Exception as e:
        print('Création superuser échouée:', e)
else:
    user.set_password('{password}')
    user.save()
    print('Mot de passe superuser mis à jour pour {email}')
"""
    run_list([sys.executable, MANAGE, "shell", "-c", code.strip()])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", default="4500")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--debug", action="store_true")
    ap.add_argument("--settings", help="ex: config.settings")
    ap.add_argument("--skip-install", dest="skip_install", action="store_true")
    ap.add_argument("--skip-makemigrations", dest="skip_makemigrations", action="store_true")
    ap.add_argument("--skip-collectstatic", dest="skip_collectstatic", action="store_true")
    ap.add_argument("--superuser-email")
    ap.add_argument("--superuser-password")
    args = ap.parse_args()

    maybe_set_settings(args.settings)
    os.environ.setdefault("PYTHONUNBUFFERED", "1")
    os.environ.setdefault("DJANGO_SECRET_KEY", os.environ.get("DJANGO_SECRET_KEY", "change-me-dev-key"))
    if args.debug:
        os.environ["DJANGO_DEBUG"] = "True"

    if not args.skip_install:
        pip_install()

    if not os.path.isfile(MANAGE):
        print("manage.py introuvable. Lance le script à la racine du projet.")
        sys.exit(1)

    if not args.skip_makemigrations:
        run_list([sys.executable, MANAGE, "makemigrations", "--noinput"])

    run_list([sys.executable, MANAGE, "migrate", "--noinput"])

    if not args.skip_collectstatic:
        run_list([sys.executable, MANAGE, "collectstatic", "--noinput"])

    if args.superuser_email and args.superuser_password:
        make_superuser(args.superuser_email, args.superuser_password)

    print(f"Démarrage du serveur sur {args.host}:{args.port} ...")
    run_list([sys.executable, MANAGE, "runserver", f"{args.host}:{args.port}"])

if __name__ == "__main__":
    main()













# import argparse, os, sys, subprocess

# BASE = os.path.dirname(os.path.abspath(__file__))
# MANAGE = os.path.join(BASE, "manage.py")
# REQ = os.path.join(BASE, "requirements.txt")

# def run_list(argv, env=None):
#     print("$", " ".join(argv))
#     p = subprocess.run(argv, env=env)
#     if p.returncode != 0:
#         sys.exit(p.returncode)

# def pip_install():
#     if os.path.isfile(REQ):
#         run_list([sys.executable, "-m", "pip", "install", "-r", REQ])
#     else:
#         print("requirements.txt introuvable, étape ignorée.")

# def maybe_set_settings(settings):
#     if settings:
#         os.environ["DJANGO_SETTINGS_MODULE"] = settings

# def make_superuser(email, password):
#     if not email or not password:
#         return
#     code = f"""
# import os, django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv('DJANGO_SETTINGS_MODULE',''))
# django.setup()
# from django.contrib.auth import get_user_model
# U = get_user_model()
# user = U.objects.filter(email='{email}').first() or U.objects.filter(username='{email}').first()
# if not user:
#     try:
#         U.objects.create_superuser(username='{email}', email='{email}', password='{password}')
#         print('Superuser créé: {email}')
#     except Exception as e:
#         print('Création superuser échouée:', e)
# else:
#     user.set_password('{password}')
#     user.save()
#     print('Mot de passe superuser mis à jour pour {email}')
# """
#     run_list([sys.executable, MANAGE, "shell", "-c", code.strip()])

# def set_integration_env(testlink_url):
#     if testlink_url:
#         os.environ["TESTLINK_URL"] = testlink_url
#     else:
#         os.environ.setdefault("TESTLINK_URL", "http://tl.digitalglue.in/index.php")

# def main():
#     ap = argparse.ArgumentParser()
#     ap.add_argument("--port", default="4500")
#     ap.add_argument("--host", default="127.0.0.1")
#     ap.add_argument("--debug", action="store_true")
#     ap.add_argument("--settings", help="ex: config.settings")
#     ap.add_argument("--skip-install", dest="skip_install", action="store_true")
#     ap.add_argument("--skip-makemigrations", dest="skip_makemigrations", action="store_true")
#     ap.add_argument("--skip-collectstatic", dest="skip_collectstatic", action="store_true")
#     ap.add_argument("--superuser-email")
#     ap.add_argument("--superuser-password")
#     ap.add_argument("--testlink-url", default=None)
#     args = ap.parse_args()

#     maybe_set_settings(args.settings)
#     os.environ.setdefault("PYTHONUNBUFFERED", "1")
#     os.environ.setdefault("DJANGO_SECRET_KEY", os.environ.get("DJANGO_SECRET_KEY", "change-me-dev-key"))
#     if args.debug:
#         os.environ["DJANGO_DEBUG"] = "True"

#     set_integration_env(args.testlink_url)

#     if not args.skip_install:
#         pip_install()

#     if not os.path.isfile(MANAGE):
#         print("manage.py introuvable. Lance le script à la racine du projet.")
#         sys.exit(1)

#     if not args.skip_makemigrations:
#         run_list([sys.executable, MANAGE, "makemigrations", "--noinput"])

#     run_list([sys.executable, MANAGE, "migrate", "--noinput"])

#     if not args.skip_collectstatic:
#         run_list([sys.executable, MANAGE, "collectstatic", "--noinput"])

#     if args.superuser_email and args.superuser_password:
#         make_superuser(args.superuser_email, args.superuser_password)

#     print(f"Démarrage du serveur sur {args.host}:{args.port} ...")
#     run_list([sys.executable, MANAGE, "runserver", f"{args.host}:{args.port}"])

# if __name__ == "__main__":
#     main()



# Username: admin

# Password: AdminPass123!



# Username: admin

# Password: admin