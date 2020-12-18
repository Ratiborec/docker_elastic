### Install

Run command below to give right permissions for filebeat file

`sudo chown 1000 filebeat/filebeat.yml`

To run stack just run command below in folder with docker-compose.yaml and appropriate folders

`docker-compose up -d`


### TODO

1. Find solution to forward variable in more pretty way

2. Realiz python script to send email on every kibana access

3. Make possibility do not make `chown` operation before run
