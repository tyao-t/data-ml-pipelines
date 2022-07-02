sudo docker image build -t "sklearn_pipeline" .
sudo docker images
sudo docker run sklearn_pipeline

cat dsdemo.json | sudo docker login -u _json_key --password-stdin https://us.gcr.io
sudo docker tag sklearn_pipeline us.gcr.io/[my_project_id]/sklearn_pipeline
sudo docker push us.gcr.io/[my_project_id]/sklearn_pipeline

kubectl apply -f pipeline.yaml