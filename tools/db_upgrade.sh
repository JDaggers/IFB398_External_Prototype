echo "Running db upgrade ..."
docker exec -it prototype bash -c "flask db upgrade"
