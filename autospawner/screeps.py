import screepsapi
import os
import sys
import yaml

cwd = os.getcwd()
path = cwd + '/.screepsas.yaml'

if not os.path.isfile(path):
    print('no settings file found')
    sys.exit(-1)

with open(path, 'r') as f:
    settings = yaml.load(f, yaml.Loader)

screepsclient = screepsapi.API(token=settings['token'])

def api_error_except(api_result):
    if 'error' in api_result:
        raise Exception(api_result['error'])
    return api_result

setattr(screepsclient, "api_error_except", api_error_except)
