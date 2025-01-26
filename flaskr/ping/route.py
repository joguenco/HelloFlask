from flaskr.ping.ping_controller import PingController


def define_routes(api):
    api.prefix = '/hello/v1'
    api.add_resource(PingController, '/ping')
