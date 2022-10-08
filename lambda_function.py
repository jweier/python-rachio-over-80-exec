# import required modules
import requests, json
import botocore 
import botocore.session 
from aws_secretsmanager_caching import SecretCache, SecretCacheConfig 
import re

def startRachio(rachioAPIKey):
	print("Starting Rachio")
	rachioURL = "https://api.rach.io/1/public/schedulerule/start"

	rachioPayload = {"id": "e9e49b85-0de7-41ff-9009-ae1cdae9fc30"}
	rachioHeaders = {
		"Content-Type": "application/json",
		"Authorization": "Bearer " + rachioAPIKey
	}

	response = requests.request("PUT", rachioURL, json=rachioPayload, headers=rachioHeaders)

def lambda_handler(event, context):
# if __name__ == "__main__":
    client = botocore.session.get_session().create_client('secretsmanager')
    cache_config = SecretCacheConfig()
    cache = SecretCache( config = cache_config, client = client)

    rachioAPIKey = cache.get_secret_string('arn:aws:secretsmanager:us-east-1:514894476795:secret:rachioAPIKey-pztCKo')
    rachioAPIKey = re.sub("{\"apikey\":\"", "", rachioAPIKey)
    rachioAPIKey = re.sub("\"}", "", rachioAPIKey)

    startRachio(rachioAPIKey)

  





