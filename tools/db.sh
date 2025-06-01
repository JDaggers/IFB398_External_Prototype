PORT=3308
HOST=localhost
USER=local
PASSWORD=password
echo "mycli mysql://$USER@$HOST:$PORT -p$PASSWORD"
mycli mysql://$USER@$HOST:$PORT -p$PASSWORD
