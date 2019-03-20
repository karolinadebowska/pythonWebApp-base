import requests

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get(
        'https://api.thecatapi.com/v1/images/search',
        headers={'x-api-key': '4afdaee1-3e5c-4e37-b331-3b2ae1fc2ddf'}
    )
    data = response.json()[0]
    print(data)
    url = data['url']
    image_id = data['id']
    return render_template('index.html', picture=url, image_id=image_id)

@app.route('/save')
def add_favourite():
    image_id = request.args.get('image_id')

    response = requests.post(
        'https://api.thecatapi.com/v1/favourites',
        headers={'x-api-key': '4afdaee1-3e5c-4e37-b331-3b2ae1fc2ddf'},
        json={
            'image_id': image_id,
            'sub_id': 'bxslhr'
        }
    )
    data = response.json()
    print(data)
    return '{}! Go back!'.format(data['message'])

@app.route('/fav')
def see_favourites():
    response = requests.get(
        'https://api.thecatapi.com/v1/favourites?limit=3',
        headers={'x-api-key': '4afdaee1-3e5c-4e37-b331-3b2ae1fc2ddf'}
    )
    data = response.json()
    print(data)
    return render_template('favourites.html', data=data)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)