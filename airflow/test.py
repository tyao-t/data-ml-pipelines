from google.cloud import bigquery
client = bigquery.Client()

sql = "select * from dsp_demo.user_scores"
client.query(sql).to_dataframe().head()