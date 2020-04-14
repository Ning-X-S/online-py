#!/usr/bin/python3
import os
import sys

server_type = ''
update = ''

if (len(sys.argv) > 1):
  server_type = sys.argv[1]
if (len(sys.argv) > 2):
  update = sys.argv[2]

# 默认走的不删除服务，直接重启一下
# 默认不更新nod_modules
def online(server_type = 'restart', update = 'update_code'):  
  os.chdir("/Users/higo/works/my-git/creat-cli-app")
  os.system("git checkout .")
  os.system("git pull")
  if update == 'update_modules':
    os.system("npm install")
  os.system("npm run build")
  if server_type == 'start':
    os.system("pm2 delete react-app")
    os.system("pm2 start ./index.js --name react-app -i 4 -- -port 7001 -path ../creat-cli-app/build")
  else:
    os.system("pm2 restart react-app")

online(server_type, update)


# os.chdir("/home/work/static-server")
# if 'start':
#   os.system("pm2 delete react-app")
#   os.system("pm2 start ./index.js --name react-app -i 4 -- -port 7001 -path ../creat-cli-app/build")
# else:
#   os.system("pm2 restart react-app")

# with cd('/home/work/creat-cli-app'):
#   run('git checkout .')
#   run('git pull')
#   run('npm install')
#   run('npm run build')
  # run('cp -rf dist/* dist_bak/')
  # run('pm2 restart react-app')