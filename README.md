# systeminfo

Using the OCP python base image:
Please set either APP_MODULE, APP_FILE or APP_SCRIPT environment variables, or create a file 'app.py' to launch your application.

To fix the permission issue on OCP:
https://access.redhat.com/solutions/2111281

# Build process

# Update Dockerfile

sudo docker build --tag tprinz/systeminfo:latest .
sudo docker run -p8080:80 tprinz/systeminfo

# Push the image to [docker.io/tprinz/systeminfo]

sudo docker push tprinz/systeminfo



sudo docker pull tprinz/systeminfo
sudo docker inspect tprinz/systeminfo

Access the script in a browser at

http://localhost:8080/cgi-bin/systeminfo.py

