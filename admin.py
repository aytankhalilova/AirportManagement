import requests, json
localhost = "http://127.0.0.1:7210"

class Admin_user:
    def __init__(self, username, pswd):
        self.username = username
        self.pswd = pswd

    def auth_admin(self):
        req_post = requests.post(localhost + '/authentication_authorization', data={'username':self.username, 'pswd':self.pswd})
        auth_token = req_post.json()
        return auth_token

    def add_flight(self, _id, c_from, c_to, t_arv, t_dpr, info, num):
        f_add = requests.post(localhost+'/flights', {'id_f':_id, 'from_city':c_from, 'to_city':c_to, 'time_arrival':t_arv, 'time_departure':t_dpr, 'info_flight':info, 'num_psg':num})
        return f_add.text

    def update_flight(self, _id, c_from, c_to, t_arv, t_dpr, info, num):
        f_update = requests.put(localhost+'/flights', {'id_f':_id, 'from_city':c_from, 'to_city':c_to, 'time_arrival':t_arv, 'time_departure':t_dpr, 'info_flight':info, 'num_psg':num})
        return f_update.text

    def delete_flight(self, _id):
        f_delete = requests.delete(localhost+'/flights', data={'id_f':_id})
        return f_delete.text

    def get_flight(self, city_from, city_to):
        f_get = requests.get(localhost+'/flights', {'from_city':city_from, 'to_city':city_to})
        json_ = json.loads(f_get.text)
        if len(json_) == 0:
            print('There isn\'t such flight... ')
        else:
            print(f_get.text)

    def get_all_flights(self):
        f_all_get = requests.get(localhost+'/flights/all')
        json_ = json.loads(f_all_get.text)
        if len(json_) == 0:
            print('There aren\'t flights for now... ')
        else:
            print(f_all_get.text)

    def end_sessn(self, token):
        delete = requests.delete(localhost+'/end_session', data={'token':token})

if __name__ == '__main__':
    username = input('Enter the username: ')
    pswd = input('Enter the password: ')
    admin = Admin_user(username, pswd)
    x = admin.auth_admin()
    token_ = x['token']   
    sess_list = x['s']   

    if token_ == 0 or token_ not in sess_list:
        print("Authentication is denied. invalid username or password. ")
    else:
        print('Authentication is successful. ')
        while True:
            process = input('Choose procedure: add, delete, update, get, get_all or end. ')
            if (process.lower() == 'get'):
                city_from = input('Enter the city of departure. ')
                city_to = input('Enter the destination.')
                admin.get_flight(city_from, city_to)

            elif (process.lower() == 'add'):
                _id = int(input('Enter flight_id(integer): '))
                city_from = input('Enter the city of departure: ')
                city_to = input('Enter the destination: ')
                departure_time = input('Enter departure time: ')
                arrival_time = input('Enter arrival time: ')
                flight_info = input('Enter information about flight: ')
                passengers_num = int(input('Enter the number of the passengers: '))
                result = admin.add_flight(_id, city_from, city_to, arrival_time, departure_time, flight_info, passengers_num)
                print(result)

            elif (process.lower() == 'delete'):
                _id = int(input('Enter the ID of the flight which will be deleted: '))
                result = admin.delete_flight(_id)
                print(result)

            elif (process.lower() == 'update'):
                _id = int(input('Enter the ID of the flight which will be changed: '))
                city_from = input('Enter the new city of departure: ')
                city_to = input('Enter the new destination: ')
                departure_time = input('Enter new departure time: ')
                arrival_time = input('Enter new arrival time: ')
                flight_info = input('Enter new information about flight: ')
                passengers_num = int(input('Enter the number of the passengers: '))
                result = admin.update_flight(_id, city_from, city_to, arrival_time, departure_time, flight_info, passengers_num)
                print(result)

            elif (process.lower() == 'get_all'):
                admin.get_all_flights()

            elif (process.lower() == 'end'):
                admin.end_sessn(token_)
                break
            else:
                print('Invalid procedure!!!')
                continue
