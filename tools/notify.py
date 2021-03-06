import requests, json, argparse
parser = argparse.ArgumentParser()
parser.add_argument('key')
parser.add_argument('application')
parser.add_argument('title')
parser.add_argument('message')
parser.add_argument('--endpoint', default='https://api.picar.us/openglass/notify/')
parser.add_argument('--priority', action='store_true')
args = vars(parser.parse_args())
requests.post(args['endpoint'], data=json.dumps({k: v for k, v in args.items() if k != 'endpoint'}))
