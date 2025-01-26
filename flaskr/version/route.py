# -*- coding: utf-8 -*-
from flaskr.version.version_controller import VersionController


def define_routes(api):
    api.prefix = '/hello/v1'
    api.add_resource(VersionController, '/version')
