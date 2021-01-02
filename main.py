from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse
import random

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airport_db.db'

class Admin(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    pswd = db.Column(db.String(50), nullable=False)

class Flight(db.Model):
    flight_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city_from = db.Column(db.String(50), nullable=False)
    city_to = db.Column(db.String(50), nullable=False)
    flight_info = db.Column(db.String(250), nullable=False)
    arrival_time = db.Column(db.String(50), nullable=False)
    departure_time = db.Column(db.String(50), nullable=False)
    passengers_num = db.Column(db.Integer, nullable=False)

class User(Resource):
    def get(self, city_from, city_to):
        f_list = []
        flights = Flight.query.filter_by(city_from = city_from, city_to=city_to).all()
        #return flights
        for flight in flights:
            flights_json = {'flight_id':flight.flight_id, 'city_from' : flight.city_from, 'city_to' : flight.city_to, 'arrival_time':flight.arrival_time, 'departure_time':flight.departure_time, 'flight_info':flight.flight_info, 'passengers_num':flight.passengers_num}
            f_list.append(flights_json)

        return f_list

sessions = []   #tokens

class AdminProcesses(Resource):
    def get(self):
        f_args = reqparse.RequestParser()
        f_args.add_argument('from_city', type=str)
        f_args.add_argument('to_city', type=str)
        args = f_args.parse_args()

        f_list = []
        flights = Flight.query.filter_by(city_from = args.from_city, city_to = args.to_city).all()
        for flight in flights:
            flights_json = {'flight_id': flight.flight_id, 'city_from': flight.city_from, 'city_to': flight.city_to, 'passengers_num':flight.passengers_num, 'flight_info':flight.flight_info, 'arrival_time':flight.arrival_time, 'departure-time':flight.departure_time}
            f_list.append(flights_json)

        return f_list

    def post(self):
        new_f_args = reqparse.RequestParser()
        new_f_args.add_argument("id_f", type=int)
        new_f_args.add_argument("from_city", type=str)
        new_f_args.add_argument("to_city", type=str)
        new_f_args.add_argument("time_arrival", type=str)
        new_f_args.add_argument("time_departure", type=str)
        new_f_args.add_argument("info_flight", type=str)
        new_f_args.add_argument("num_psg", type=int)
        args = new_f_args.parse_args()

        old_flight = Flight.query.filter_by(flight_id=args.id_f).first()
        if (old_flight):
            return 'This flight ID is already exist!!! Try to update it or enter new ID. '
        else:
            new_flight = Flight(flight_id=args.id_f, city_from=args.from_city, city_to=args.to_city, arrival_time=args.time_arrival, departure_time=args.time_departure, flight_info=args.info_flight, passengers_num=args.num_psg)
            db.session.add(new_flight)
            db.session.commit()
            return 'Flight successfully added! '

    def put(self):
        update_f_args = reqparse.RequestParser()
        update_f_args.add_argument('id_f', type=int)
        update_f_args.add_argument('from_city', type=str)
        update_f_args.add_argument('to_city', type=str)
        update_f_args.add_argument('time_arrival', type=str)
        update_f_args.add_argument('time_departure', type=str)
        update_f_args.add_argument('info_flight', type=str)
        update_f_args.add_argument('num_psg', type=int)
        args = update_f_args.parse_args()

        flight = Flight.query.filter_by(flight_id=args.id_f).first()
        if (flight):
            flight.flight_id = args.id_f
            flight.city_from = args.from_city
            flight.city_to = args.to_city
            flight.arrival_time = args.time_arrival
            flight.departure_time = args.time_departure
            flight.flight_info = args.info_flight
            flight.passengers_num = args.num_psg

            db.session.commit()
            return 'Flight successfully updated! '
        else:
            return 'Flight doesn\'t  exist!!! '

    def delete(self):
        del_f_args = reqparse.RequestParser()
        del_f_args.add_argument('id_f', type=int)
        args = del_f_args.parse_args()

        flight = Flight.query.filter_by(flight_id = args.id_f).first()
        if (flight):
            db.session.delete(flight)
            db.session.commit()
            return 'Flight successfully deleted! '
        else:
            return 'Flight doesn\'t exist!!! '

class AuthProcesses(Resource):
    def post(self):
        auth_token = ''
        admin_login_args = reqparse.RequestParser()
        admin_login_args.add_argument('username', type=str)
        admin_login_args.add_argument('pswd', type=str)
        args = admin_login_args.parse_args()

        admin = Admin.query.filter_by(username = args.username, pswd = args.pswd).first()
        if (admin):
            new_token = random.randint(1, 1000000)
            sessions.append(new_token)
            return {'token' : new_token, 's':sessions}
        else:
            return {'token': 0, 's' : sessions}

class AllFlights(Resource):
    def get(self):
        f_list = []
        flights = Flight.query.all()
        # return flights
        for flight in flights:
            flights_json = {'flight_id': flight.flight_id, 'city_from': flight.city_from, 'city_to': flight.city_to, 'arrival_time':flight.arrival_time, 'departure_time':flight.departure_time, 'flight_info':flight.flight_info, 'passengers_num':flight.passengers_num}
            f_list.append(flights_json)

        return f_list

class EndSession(Resource):
    def delete(self):
        arg = reqparse.RequestParser()
        arg.add_argument('token', type=int)
        args = arg.parse_args()

        if args.token in sessions:
            sessions.remove(args.token)

if __name__ == '__main__':
    api.add_resource(User,'/flights/<string:city_from>/<string:city_to>')
    api.add_resource(AuthProcesses, '/authentication_authorization')
    api.add_resource(AdminProcesses, '/flights')
    api.add_resource(EndSession, '/end_session')
    api.add_resource(AllFlights, '/flights/all')
    '''
    CREATE FIRST DATABASE FOR FLIGHT
    db.create_all()
    first_f = Flight(flight_id=1, city_from='Doha', city_to='Milan', flight_info='Highest hygiene standards', arrival_time='18 Jan 08:10', departure_time='18 Jan 12:45', passengers_num=365)
    db.session.add(first_f)
    db.session.commit()
    '''
    app.run(debug = True)
