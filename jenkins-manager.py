import jenkins
import argparse
import sys

# Ustawienia Jenkins
JENKINS_URL = 'http://localhost:8080'
USERNAME = 'admin'
PASSWORD = 'admin'  # lub API token

try:
    server = jenkins.Jenkins(JENKINS_URL, username=USERNAME, password=PASSWORD)
    user = server.get_whoami()
    version = server.get_version()
    print(f"Połączono z Jenkins {version} jako {user['fullName']}")
except Exception as e:
    print(f"Błąd połączenia z Jenkins: {e}")
    sys.exit(1)


def list_jobs():
    try:
        jobs = server.get_jobs()
        print("Dostępne zadania:")
        for job in jobs:
            print(f"- {job['name']}")
    except Exception as e:
        print(f"Błąd podczas listowania zadań: {e}")


def job_status(job_name):
    try:
        build_info = server.get_job_info(job_name)['lastBuild']
        if build_info is None:
            print(f"Zadanie '{job_name}' nie ma jeszcze żadnych buildów.")
            return
        last_build_number = build_info['number']
        last_build_data = server.get_build_info(job_name, last_build_number)
        print(f"Ostatni build zadania '{job_name}':")
        print(f"  Numer: {last_build_number}")
        print(f"  Status: {last_build_data['result']}")
        print(f"  URL: {last_build_data['url']}")
    except Exception as e:
        print(f"Błąd pobierania statusu zadania: {e}")


def build_job(job_name):
    try:
        server.build_job(job_name)
        print(f"Uruchomiono zadanie: {job_name}")
    except Exception as e:
        print(f"Błąd uruchamiania zadania: {e}")


parser = argparse.ArgumentParser(description="Zarządzanie zadaniami Jenkins")
parser.add_argument('command', choices=['list', 'status', 'build'], help="Dostępne komendy")
parser.add_argument('--job', help="Nazwa zadania Jenkins")

args = parser.parse_args()

if args.command == 'list':
    list_jobs()
elif args.command == 'status':
    if not args.job:
        print("Podaj nazwę zadania za pomocą --job")
    else:
        job_status(args.job)
elif args.command == 'build':
    if not args.job:
        print("Podaj nazwę zadania za pomocą --job")
    else:
        build_job(args.job)
