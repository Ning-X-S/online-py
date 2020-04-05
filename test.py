#!/usr/bin/python3
import os

os.system("cd /home/work/creat-cli-app")
os.system("git pull")
os.system("npm install")
os.system("npm run build")

# with cd('/home/work/creat-cli-app'):
#   run('git checkout .')
#   run('git pull')
#   run('npm install')
#   run('npm run build')
  # run('cp -rf dist/* dist_bak/')
  # run('pm2 restart react-app')