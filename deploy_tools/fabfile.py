from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
from will_legislate_for_money.secrets import *
import random
import pdb

REPO_URL = 'https://github.com/meyerhoferc/will-legislate-for-money'

def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    source_folder = site_folder + '/source'
    _create_directory_structure_if_necessary(site_folder)
    _update_secrets(source_folder)
    _get_latest_source(source_folder)
    _update_settings(source_folder, env.host)
    _update_virtualenv(source_folder)
    _update_database(source_folder)
    _update_images(source_folder)
    _update_static_files(source_folder)

def _create_directory_structure_if_necessary(site_folder):
    for subfolder in ('database', 'static', 'virtualenv', 'source'):
        run(f'mkdir -p {site_folder}/{subfolder}')

def _get_latest_source(source_folder):
    if exists(source_folder + '/.git'):
        run(f'cd {source_folder} && git pull origin master')
    else:
        run(f'git clone {REPO_URL} {source_folder}')
        current_commit = local("git log -n 1 --format=%H", capture=True)
        run(f'cd {source_folder} && git reset --hard {current_commit}')

def _update_settings(source_folder, site_name):
    settings_path = source_folder + '/will_legislate_for_money/settings.py'
    sed(settings_path, "DEBUG = True", "DEBUG = False")
    sed(settings_path, 'ALLOWED_HOSTS =.+$', f'ALLOWED_HOSTS = ["{site_name}"]')
    secret_key_file = source_folder + '/will_legislate_for_money/secret_key.py'
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, f'SECRET_KEY = "{key}"')
        append(settings_path, '\nfrom .secret_key import SECRET_KEY')

def _update_virtualenv(source_folder):
    virtualenv_folder = source_folder + '/../virtualenv'
    if not exists(virtualenv_folder + '/bin/pip'):
        run(f'python3.6 -m venv {virtualenv_folder}')
    run(f'{virtualenv_folder}/bin/pip install -r {source_folder}/requirements.txt')
    run(f'{virtualenv_folder}/bin/pip install requests')
    run(f'{virtualenv_folder}/bin/pip install social-auth-app-django')
    run(f'{virtualenv_folder}/bin/pip install django-nvd3')
    run(f'{virtualenv_folder}/bin/pip install django-bower')

def _update_secrets(source_folder):
    current_open_secrets = OPEN_SECRETS_KEY
    current_propublica = PROPUBLICA_KEY
    current_twitter_key = TWITTER_KEY
    current_twitter_secret = TWITTER_SECRET
    secrets_file = source_folder + '/will_legislate_for_money/secrets.py'
    if not exists(secrets_file):
        run(f'touch {source_folder}/will_legislate_for_money/secrets.py')
    secrets_file = source_folder + '/will_legislate_for_money/secrets.py'
    run(f'echo "OPEN_SECRETS_KEY = \'{current_open_secrets}\'" > {secrets_file}')
    run(f'echo "PROPUBLICA_KEY = \'{current_propublica}\'" > {secrets_file}')
    run(f'echo "TWITTER_KEY = \'{current_twitter_key}\'" > {secrets_file}')
    run(f'echo "TWITTER_SECRET = \'{current_twitter_secret}\'" > {secrets_file}')

def _update_static_files(source_folder):
    virtualenv_folder = source_folder + '/../virtualenv'
    run(f'cd {source_folder} && {virtualenv_folder}/bin/python manage.py bower install')
    run(f'cd {source_folder} && ../virtualenv/bin/python manage.py collectstatic --noinput')

def _update_database(source_folder):
    run(f'cd {source_folder} && ../virtualenv/bin/python manage.py migrate --noinput')

def _update_images(source_folder):
    images_folder = source_folder + '/pubic_officials/static/public_officials/images/profiles'
    if not exists(images_folder):
        run(f'cd {source_folder} && mkdir public_officials/static/public_officials/images/profiles')
    run(f'cd {source_folder} && ../virtualenv/bin/python manage.py get_images')
