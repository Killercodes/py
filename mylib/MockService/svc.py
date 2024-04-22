from bottle import Bottle, run, response, request, template
import json

app = Bottle()


@app.route('/help')
@app.route('/')
def hello():
    return template("index")


@app.route('/<path:path>')
def catch_all(path):
    keys = list(request.query.keys())
    if keys:
        first_key = keys[0]
        first_value = request.query.get(first_key)
        print(f'First Key: {first_key}, First Value: {first_value}')

        if request.headers.get('Content-Type') == 'application/json':
            with open(f'{path}/{first_value}.json', 'r') as file:
                jdata = file.read()
            response.content_type = 'application/json'
            return json.dumps({"data": jdata})
        else:
            with open(f'{path}/{first_value}.xml', 'r') as file:
                xdata = file.read()
            response.content_type = 'application/xml'
            return xdata



#run
if __name__ == "__main__":
    run(app, host='localhost', port=8080,reloader=True)
    
