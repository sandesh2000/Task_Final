Workspace Directory: myFlaskApp
Python Virtual env folder: flaskproject
Flask: To create our web application
Gunicorn: To provide an wsgi entrypoint for the flask application
Nginx: To create reverse proxy/loadbalancing, which will distribute client requests among Flask servers
Docker: To scale our servers quickly

wsgi.py: Our flask application

templates/index.html: Html content we want flask should render and display.

Flask will run successfully,but now we want to scale this, we can do this using docker.

requirements.txt: package to be installed in the flask container

Dockerfile: To launch our Flask application server.
(We have binded it to port 5000 of container)
(Note: Flask default server is just for development, it shouldn't be used for production, that's why 
we will use a production gateway interface webserver i.e. Gunicorn)

docker-compose.yml: To launch multiple services defined in just 1 click
(1st service is to launch the flask container, we have provided the context: app, i.e. where Dockerfile is located for the flask app)
docker-compose up -d --scale app=3 (No. of flask service containers we want)
We have given port no. as 5000, i.e. on which port of containers the flask app should run.
As we launch , all the containers are mapped to random ports of the host machine.

We want to have a single hostname of our application instead of multiple ports of containers, 
we can do so by concept of Loadbalancing using nginx server.

nginx.conf: nginx server requires its configuration file
(proxy_pass http://app:5000 -> We don't know the ip of flask containers, as docker discovers host via the service name in docker-compose, here: app, docker uses container id as the hostname )

I have used autocannon tool for the benchmarking of our architecture, which provides statistics for request and latency.

I did the same task on both t2.micro as well as t2.medium to have a better comparison.

Apart from the given task, now I am working on the same to integrate it with Prometheus and Grafana for Real-time monitoring on a beautiful Dashboards(provided by Grafana) of our server running in AWS.

Thank You for this task, it was really interesting, hoping for the best.