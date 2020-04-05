#!/usr/bin/python3
import os

os.chdir("/home/work/creat-cli-app")
os.system("git checkout .")
os.system("git pull")
os.system("npm install")
os.system("npm run build")
os.chdir("/home/work/static-server")
os.system("pm2 restart ./index.js --name react-app -i 4 -- -port 7001 -path ../creat-cli-app/build")

# with cd('/home/work/creat-cli-app'):
#   run('git checkout .')
#   run('git pull')
#   run('npm install')
#   run('npm run build')
  # run('cp -rf dist/* dist_bak/')
  # run('pm2 restart react-app')