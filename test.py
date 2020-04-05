#!/usr/bin/python3

with cd('/home/work/creat-cli-app'):
  run('git checkout .')
  run('git pull')
  run('npm install')
  run('npm run build')
  # run('cp -rf dist/* dist_bak/')
  # run('pm2 restart react-app')