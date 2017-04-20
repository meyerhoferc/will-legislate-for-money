Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.6
* virtualenv + pip
* Git

eg, on Ubuntu:

    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt-get install nginx git python36 python3.6-venv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
         ├── database
         ├── source
         ├── static
         └── virtualenv

We can do a commit for those:

$ git add deploy_tools
$ git status # see three new files
$ git commit -m "Notes and template config files for provisioning"

Our source tree will now look something like this:

.
├── deploy_tools
│   ├── gunicorn-systemd.template.service
│   ├── nginx.template.conf
│   └── provisioning_notes.md
├── functional_tests
│   ├── [...]
├── public_officials
│   ├── __init__.py
│   ├── models.py
│   ├── [...]
│   ├── static
│   │   ├── base.css
│   │   └── bootstrap
│   │       ├── [...]
│   ├── templates
│   │   ├── base.html
│   │   ├── [...]
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
└── will_legislate_for_money
    ├── [...]
