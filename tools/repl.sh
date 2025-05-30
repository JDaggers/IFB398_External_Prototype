CONTAINER=proto
docker exec -it $CONTAINER pip install flask-shell-ipython

# Create ipython profile and enable autoreload
docker exec -it $CONTAINER bash -c 'mkdir -p ~/.ipython/profile_default/'
docker exec -it $CONTAINER bash -c 'touch ~/.ipython/profile_default/ipython_config.py'
docker exec -it $CONTAINER bash -c 'echo "c.InteractiveShellApp.exec_lines = []" >> ~/.ipython/profile_default/ipython_config.py'
docker exec -it $CONTAINER bash -c 'echo "c.InteractiveShellApp.exec_lines.append(\"%load_ext autoreload\")" >> ~/.ipython/profile_default/ipython_config.py'
docker exec -it $CONTAINER bash -c 'echo "c.InteractiveShellApp.exec_lines.append(\"%autoreload 2\")" >> ~/.ipython/profile_default/ipython_config.py'

docker exec -it $CONTAINER flask shell
