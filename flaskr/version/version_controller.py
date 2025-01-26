# -*- coding: utf-8 -*-
from flask_restful import Resource
import platform
from flaskr.version.version_service import get_version


class VersionController(Resource):
    def get(self):
        return {
            'application': {
                'name': 'HelloFlask',
                'author': 'Jorge Luis',
                'version': '1.0.0',
                'versionOS': f'{platform.system()} {platform.release()}',
                'versionDatabase': get_version(),
                'versionPython': platform.python_version(),
            }
        }
