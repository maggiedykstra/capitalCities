# capitalCities Project
### DS2002 Assignment
### Author: Maggie Dykstra

This project is an API that provides the local time for capital cities. The API is hosted on a Google Cloud Platform (GCP) VM and is accessible via a URL.

## Working API URL
You can access the API using the following IP address:
[http://34.85.138.229:5001](http://34.85.138.229:5001)

## How to Run the API

1. **SSH into your GCP VM** where the API is hosted.
2. Navigate to the directory containing the `capital.py` file.
3. Run the following command to start the API:
   python3 capital.py

## How to Call the API

Use the following command: curl -H "Authorization: Bearer TOKEN" http://34.85.138.229:5001/api/time?city=CapitalName

Replace CapitalName with the name of any capital city you would like to get the time of.

Replace TOKEN with the correct token for the authorization

One example of correct input would be:  curl -H "Authorization: Bearer supersecrettoken123" http://34.85.138.229:5001/api/time?city=Cairo

This would output:

{
  "city": "Cairo",
  "local_time": "2025-04-20 22:41:33"
}

  
