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
def online(server_type = 'restart', update = 'update_modules')
  os.chdir("/home/work/service/react-service")
  os.system("git checkout .")
  os.system("git pull")
  if update == 'update_modules':
    os.system("npm install")
  os.chdir("/home/work/service/react-service")
  if server_type == 'start':
    os.system("pm2 delete react-service")
    os.system("pm2 start start.json --env production")
  else:
    os.system("pm2 restart react-service")

online(server_type, update)
