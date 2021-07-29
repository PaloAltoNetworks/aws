#!/usr/bin/env bash

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>SSH attempt</title>'
echo '</head>'
echo '<body>'
echo '<H1>'
echo 'SSH from web server to DB server attempt launched.'
echo '</H1><BR><BR>'
echo '<button style="color: #F08; font-weight: bold; font-size: 150%; text-transform: uppercase;" onclick="goBack()">Return to Attack Launch Page</button>'

echo '<script>'
echo 'function goBack() {'
echo '    window.history.back();'
echo '}'
echo '</script>'
echo '</body>'
echo '</html>'
ssh -o ConnectTimeout=2 root@DB-IP-ADDRESS

