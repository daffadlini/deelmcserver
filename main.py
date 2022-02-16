import os, time, subprocess, signal

os.system('heroku-php-apache2 &')
print("**script**: starting web")
time.sleep(10)
os.system('nohup node fetchworld.js > js.out & ')
print("**script**: fetching world...")
time.sleep(2)

while True:
    time.sleep(1)
    result = open('js.out', 'r').read().find('fetched world folder')
    if result > -1:
        break

print("**script**: world fetched!")
time.sleep(1)
os.system('unzip -o world.zip')
time.sleep(5)
print("**script**: starting server")
os.system('nohup java -Xmx1G -jar server.jar > nohup.out &')

while True:
    time.sleep(10)
    result = open('nohup.out', 'r').read().find('Done')
    if result > -1:
        break
        
print("**script**: server has started!")
time.sleep(10)
print("**script**: starting ngrok tcp")
os.system('ngrok tcp -region us 25565 &')
time.sleep(10)

while True:
    print("**script**: saving world...")
    os.system('zip -FSr world.zip world')
    time.sleep(5)
    os.system('node savetodb.js')
    print("**script**: world saved!")
    time.sleep(10)


