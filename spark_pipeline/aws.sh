#!/bin/bash

aws s3api create-bucket --bucket spark_pipeline --region us-east-1
aws s3 ls

wget https://github.com/bgweber/Twitch/raw/master/Recommendations/games-expand.csv
aws s3 cp games-expand.csv s3://spark_pipeline/csv/games-expand.csv

aws s3 cp game_plays.csv s3://spark_pipeline/csv/game_plays.csv
aws s3 cp game_skater_stats.csv s3://spark_pipeline/csv/game_skater_stats.csv
aws s3 ls  s3://spark_pipeline/csv/

aws s3 ls s3://spark_pipeline/avro/game_skater_stats/
