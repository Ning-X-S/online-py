#!/usr/bin/python3
import os
import sys
name = sys.argv[1]
print('脚本参数为：', name)
os.chdir("/home/work/creat-cli-app")
os.system("git checkout .")
os.system("git pull")
os.system("npm install")
os.system("npm run build")
if 'start':
  os.system("pm2 delete react-app")
  os.system("pm2 start ./index.js --name react-app -i 4 -- -port 7001 -path ../creat-cli-app/build")
else:
  os.system("pm2 restart react-app")

# with cd('/home/work/creat-cli-app'):
#   run('git checkout .')
#   run('git pull')
#   run('npm install')
#   run('npm run build')
  # run('cp -rf dist/* dist_bak/')
  # run('pm2 restart react-app')