

# Heavily based on the fabfile for Plan Your Picnic (https://github.com/daxtens/planyourpicnic)

from fabric.api import *

def setup():
    local("pip install bottle")
    local("pip install psycopg2")
    local("pip install simplekml pykml lxml") # check these are all necessary?
    #local("pip install pyproj")

    # Syntax checkers/cleaners
    local("pip install pep8")
    #local("easy_install http://closure-linter.googlecode.com/files/closure_linter-latest.tar.gz")
    
    # Database
    local("sudo -u postgres psql -f tools/create_db.sql")
    local("sudo -u postgres psql -f tools/init_db.sql whereshouldi")
    local("tools/setup_wsi.py")


def init_ec2():
    run("sudo apt-get update; sudo apt-get upgrade -y")
    run("sudo apt-get install -y supervisor nginx apache2-")
    run("sudo apt-get install -y python-virtualenv python-dev postgresql-9.3 postgis postgresql-9.3-postgis-2.1 postgresql-contrib-9.3 libpq-dev git fabric phppgadmin libxml2-dev libxslt1-dev postgresql-client-9.3 python-pip")
    run("[ -e /home/wsi ] || sudo useradd -m wsi")
    run("sudo rm -rf /home/wsi/whereshouldi")
    run("sudo -u wsi git clone git://github.com/ajdlinux/govhack2014.git /home/wsi/whereshouldi")
    run("cd /home/wsi/whereshouldi; sudo fab setup")
    #run("cd /home/wsi/whereshouldi; sudo tools/setup_wsi.py")
    run("""cat > /tmp/wsi.conf << __EOF__
[program:wsi]
user=wsi
command=/home/wsi/whereshouldi/main.py
autostart=true
autorestart=true
__EOF__""")
    run("sudo mv /tmp/wsi.conf /etc/supervisor/conf.d/")
    run("sudo supervisorctl reread")
    run("sudo supervisorctl reload") #start wsi")
    run("""cat > /tmp/default << __EOF__
upstream wsi {
        server 127.0.0.1:8080;
}

server {
        root /home/wsi/whereshouldi;
        index index.html index.htm;

        server_name whereshouldi.donnellan.id.au;

        location / {
                proxy_pass  http://wsi;
                proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
                proxy_redirect off;
                proxy_buffering off;
                proxy_set_header        Host            \\\$host;
                proxy_set_header        X-Real-IP       \\\$remote_addr;
                proxy_set_header        X-Forwarded-For \\\$proxy_add_x_forwarded_for;
                access_log /var/log/nginx/access.log;
        }
}
__EOF__""")
    run("sudo mv /tmp/default /etc/nginx/sites-available")
    run("sudo service nginx restart")

def update_ec2():
    run("sudo rm -rf /home/wsi/whereshouldi")
    run("sudo -u wsi git clone git://github.com/ajdlinux/govhack2014.git /home/wsi/whereshouldi")
