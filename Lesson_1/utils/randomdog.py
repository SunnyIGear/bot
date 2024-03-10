import requests


def dog():
    url = 'https://random.dog/woof.json'
    response = requests.get(url)
    if response.status_code:
        data = response.json()
        return (data.get('image'))



if __name__ == '__main__':
    dog()