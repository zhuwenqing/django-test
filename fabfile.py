from fabric.api import local
def prepare_deploy():
    local("./manage.py test mysite")
    local("git add -p && git commit")
    local("git push")