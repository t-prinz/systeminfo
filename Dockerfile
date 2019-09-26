# Use an official RHEL runtime as a parent image
#FROM registry.access.redhat.com/rhel7.6
FROM docker.io/centos

# Add necessary packages
RUN yum install -y net-tools httpd

# Set the working directory to /app
WORKDIR /app

# Copy the application to the cgi-bin directory
ADD systeminfo.py /var/www/cgi-bin/

# Install any needed packages specified in requirements.txt
#RUN pip install -r requirements.txt

# Change the listening port for the web server
#RUN sed -i -e 's/^Listen 80/Listen 8080/' /etc/httpd/conf/httpd.conf

# Make the listening port available to the world outside this container
#EXPOSE 8080
EXPOSE 80

# Define environment variable
#ENV NAME World

# Change to run as the apache user
#USER apache

# Run app.py when the container launches
##CMD ["python", "app.py"]
CMD ["/usr/sbin/httpd", "-DFOREGROUND"]
