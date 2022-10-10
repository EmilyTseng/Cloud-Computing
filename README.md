# Cloud-Computing
 docker run --name mydba -p 8081:80 -d my_dba
 docker run --name mydba -p 8081:80 -d my_dba
 dba % docker build -t my_dba .
 docker run --name mydba -p 8081:80 -d my_dba
 docker build -t my_dba . 
 cd ..
 cd db
 docker build -t my_db .
 docker network      
 docker network ls
 docker build -t my_django .
 docker run -it -p8000:8000 -v $(pwd)/app:/app my_django /bin/bash
 
 root@275358f0ce86:/app# ls
 root@275358f0ce86:/app# touch text.txt
 root@275358f0ce86:/# django-admin startproject app
 root@275358f0ce86:/# docker run -it -p8000:8000 -v $(pwd)/app:/app my_django /bin/bash
root@275358f0ce86:/# cd app
root@275358f0ce86:/app# django-admin startproject app
root@275358f0ce86:/app# python manage.py runserver 0.0.0.0:8000
python: can't open file '/app/manage.py': [Errno 2] No such file or directory
root@275358f0ce86:/app# cd ..
root@275358f0ce86:/# python manage.py runserver 0.0.0.0:8000

## db
docker run --name mydb -itd -p5432:5432 my_db
docker network create network
docker network ls  
docker run --name mydb2 --network mynetwork -p 8081:80 -d my_dba
docker run --name mydb2 --network mynetwork -itd -p5432:5432 my_db
docker run --name mydb2 --network mynetwork -itd -p5432:5432 my_db 
