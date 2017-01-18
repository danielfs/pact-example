from bottle import route, response, run

state_data = ""

@route('/', method='GET')
def root():
    response.content_type = 'application/json'
    return {"greeting": "Hello"}

@route('/fail', method='GET')
def fail():
    response.content_type = 'application/json'
    response.status = 201
    return {"greeting": "Oh noes!"}

@route('/provider-states', method='GET')
def provider_states():
    response.content_type = 'application/json'
    return {
        "me": ["quick"],
        "anotherclient": ["quick"]
    }

@route('/provider-state', method='POST')
def provider_state():
    state_data = "State data!"
    response.status = 201
    response.content_type = 'application/json'
    return {"greeting": "State set"}

@route('/somestate', method='GET')
def some_state():
    response.content_type = 'application/json'
    return {"greeting": "State data!"}

run(host='0.0.0.0', port=4000)
