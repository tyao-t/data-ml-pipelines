sudo service docker start
sudo docker ps
sudo docker image build -t "echo_service" .
sudo docker images
cat creds.json | sudo docker login -u _json_key --password-stdin https://us.gcr.io
sudo docker tag echo_service us.gcr.io/[gcp_account]/echo_service 
sudo docker push us.gcr.io/[gcp_account]/echo_service
