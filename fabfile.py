from fabric.api import *

from fabric.contrib.files import exists

env.use_ssh_config = True


HOSTS = {
    'dev': 'ubuntu@52.221.179.22',
    'prod': 'ubuntu@52.221.179.22'
}

"""
    Run by: fab deploy:dev or fab deploy:prod
"""

def deploy(mode):
    host_string = HOSTS[mode.lower()]
    dir = "." if mode == 'dev' else 'prod-deploy-dir'
    with settings(host_string=host_string):
        run ('mkdir -p ~/bundesliga-api')
        put(dir + '/docker-compose.yml', '~/bundesliga-api')
        put(dir + '/*.env', '~/bundesliga-api')
        put(dir + '/nginx', '~/bundesliga-api')
        with cd('~/bundesliga-api'):
            run('docker-compose pull')
            run('docker-compose build')
            run('docker-compose stop')
            run('docker-compose rm -f')
            run('docker-compose up -d')
