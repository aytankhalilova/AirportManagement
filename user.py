import requests, json
localhost = "http://127.0.0.1:7210"

class User:
    def __init__(self, city_from, city_to):
        self.city_from = city_from
        self.city_to = city_to

    def get_flights(self):
        url = localhost+'/flights/'+self.city_from+'/'+self.city_to;
        req_url = requests.get(url)
        json_ = json.loads(req_url.text)
        if len(json_) == 0:
            print('This flight doesn\'t exist!!! ')
        else:
            print(req_url.text)

if __name__ == '__main__':
    city_from = input('Enter the city of departure: ')
    city_to = input('Enter the destination: ')
    user = User(city_from, city_to)
    user.get_flights()
