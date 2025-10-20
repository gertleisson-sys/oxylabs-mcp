import requests
import json

# Oxylabs API credentials
username = "leisson_vBsS6"
password = "Syncmaster550sss="

# API endpoint
url = "https://realtime.oxylabs.io/v1/queries"

# Request payload
payload = {
    "source": "google_search",
    "query": "adidas",
    "geo_location": "California,United States",
    "parse": True
}

# Make the request
print("Testing Oxylabs Web Scraper API...")
print(f"Query: {payload['query']}")
print(f"Location: {payload['geo_location']}")
print("-" * 50)

try:
    response = requests.post(
        url,
        auth=(username, password),
        json=payload,
        timeout=30
    )
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print("\n✅ API Request Successful!")
        print(f"\nJob ID: {data.get('job', {}).get('id', 'N/A')}")
        print(f"Status: {data.get('job', {}).get('status', 'N/A')}")
        
        # Display some results if available
        results = data.get('results', [])
        if results and len(results) > 0:
            content = results[0].get('content', {})
            organic_results = content.get('results', {}).get('organic', [])
            
            print(f"\nFound {len(organic_results)} organic search results")
            print("\nTop 3 Results:")
            for i, result in enumerate(organic_results[:3], 1):
                print(f"\n{i}. {result.get('title', 'N/A')}")
                print(f"   URL: {result.get('url', 'N/A')}")
                print(f"   Description: {result.get('desc', 'N/A')[:100]}...")
    else:
        print(f"\n❌ API Request Failed")
        print(f"Response: {response.text}")
        
except Exception as e:
    print(f"\n❌ Error: {str(e)}")
