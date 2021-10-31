# from flask import Flask, request
# from flask_restful import Resource, Api
# from json import dumps
# from flask.ext.jsonpify import jsonify

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Server Works!'

@app.route('/greet')
def say_hello():
    return 'Hello from Server'

# app = Flask(__name__)
# # api = Api(app)

# class Example(Resource):
#     def get(self):
#         return {'hola'}

# class Employees(Resource):
#     def get(self):
#         query = conn.execute("select * from employees") # This line performs query and returns json result
#         return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

# class Tracks(Resource):
#     def get(self):
#         query = conn.execute("select trackid, name, composer, unitprice from tracks;")
#         result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
#         return jsonify(result)

# class Employees_Name(Resource):
#     def get(self, employee_id):
#         query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
#         result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
#         return jsonify(result)

# api.add_resource(Employees, '/employees') # Route_1
# api.add_resource(Tracks, '/tracks') # Route_2
# api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3

# api.add_resource(Example, '/example')

# if __name__ == '__main__':
#      app.run(port='8080')