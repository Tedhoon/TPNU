# 부산대학교 생명자원과학대학 커뮤니티 SPNU

## deploy 버전

## domain 
```shell
spnu.net
```

## deploy command
```shell
sudo apt-get update
sudo apt-get install build-essential
sudo apt-get install python3
sudo apt-get install python3-pip
sudo pip3 install --upgrade pip
ssh-keygen -t rsa
cat /home/ubuntu/.ssh/id_rsa.pub
git clone ssh
sudo apt-get install virtualenv
cd /경로
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirments.txt
runserver << 선택

pip install uwsgi 
vi uwsgi.ini

[uwsgi]
chdir=/home/ubuntu/{프로젝트 폴더}
module={프로젝트 내 파일이름}.wsgi:application
master=True
pidfile=/tmp/project-master.pid
vacuum=True
max-requests=5000
daemonize=/home/ubuntu/{프로젝트 폴더}/django.log
home=/home/ubuntu/{프로젝트 폴더}/venv
virtualenv=/home/ubuntu/{프로젝트 폴더}/venv
socket=/home/ubuntu/{프로젝트 폴더}/uwsgi.sock
chmod-socket=666



[uwsgi]
chdir=/home/ubuntu/SPNU_DP
module=TPNU.wsgi:application
master=True
pidfile=/tmp/project-master.pid
vacuum=True
max-requests=5000
daemonize=/home/ubuntu/SPNU_DP/django.log
home=/home/ubuntu/SPNU_DP/venv
virtualenv=/home/ubuntu/SPNU_DP/venv
socket=/home/ubuntu/SPNU_DP/uwsgi.sock
chmod-socket=666

uwsgi --ini uwsgi.ini
sudo apt-get install nginx
sudo vi /etc/nginx/nginx.conf
-> upstream django {
	server unix:/home/ubuntu/SPNU_DP/uwsgi.sock;
	}

sudo vi /etc/nginx/site-enabled/default
-> location  {
	include	


}
그리고 static,media 루트 설정

34분 32초



sudo service nginx restart



---------------postgresql---------------



sudo apt-get install libpq-dev
sudo apt-get install python3-psycopg2
sudo apt-get install postgresql
안되면 sudo apt-get update

관리자 계정 들어가기
sudo -u postgres pqsl

postgres=# ALTER USER postgres WITH ENCRYPTED PASSWORD 'password'
;
CREATE DATABASE spnu;

GRANT ALL PRIVILEGES ON DATABASE spnu TO postgres;

sudo /etc/init.d/postgresql restart

여기서 가상환경에서 pip install psycopg2
해주고 마이그레이션
마이그레이트

슈퍼유저 생성해주고

데이터 베이스 확인
sudo -i -u postgres
psql
\l
하면 데이터베이스 나오고
\c spnu




수정 및 배포
uwsgi --ini uwsgi.ini (django와의 연결 업데이트)
sudo service nginx reload
sudo service nginx restart

```