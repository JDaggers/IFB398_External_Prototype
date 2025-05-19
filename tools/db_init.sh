echo "Granting permissions to 'local'"
docker exec -it proto_db mariadb -uroot -proot_password -e "GRANT ALL PRIVILEGES ON proto.* TO 'local'@'%'"
echo "Runnning db init ..."
docker exec -it prototype bash -c "flask db init"
