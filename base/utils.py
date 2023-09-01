import requests

def get_random_activity():
    url = 'https://www.boredapi.com/api/activity'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['activity']
    else:
        return 'Something interesting'
    
