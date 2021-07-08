#!/usr/bin/env bash

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>brute force</title>'
echo '</head>'
echo '<body>'
echo '<H1>'
echo 'Brute force MySQL root password attempt launched.'
echo '</H1><BR><BR>'
echo '<button style="color: #F08; font-weight: bold; font-size: 150%; text-transform: uppercase;" onclick="goBack()">Return to Attack Launch Page</button>'

echo '<script>'
echo 'function goBack() {'
echo '    window.history.back();'
echo '}'
echo '</script>'
echo '</body>'
echo '</html>'
COUNTER=0
  while [  $COUNTER -lt 250 ]; do
    mysql -u user1 -h DB-IP-ADDRESS -pwrong demo --ssl-mode=DISABLED
    let COUNTER=COUNTER+1
  done
