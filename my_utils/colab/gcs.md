

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-25 23:35:01
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-25 23:35:02
 * @Description:
 * @TODO::
 * @Reference:https://www.kaggle.com/notebooks/welcome
-->
# Set your own project id here
PROJECT_ID = 'your-google-cloud-project'
from google.cloud import automl_v1beta1 as automl
automl_client = automl.AutoMlClient()
from google.cloud import storage
storage_client = storage.Client(project=PROJECT_ID)
from google.cloud import bigquery
bigquery_client = bigquery.Client(project=PROJECT_ID)
