# Cloud-Computing Command line

Command line:

 % cd Desktop 
Desktop % ls
Week_4 % ls
Week_4 % cd api 
api % ls
cd code
code % python3 api.py 

docker-compose up
docker run -it python

docker compose up

code % ls
code % cd ..
api % ls
api % docker build -t test1 .      
api % docker run --name api --network network -p 5000:5000 test1

consumer % docker build -t test2  .
consumer % docker run --network network -p 80:80 test2
