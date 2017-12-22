import os

production = os.environ.get('IMAGINARIUM_ENV', 'DEV') == 'PROD'
port = os.environ.get('IMAGINARIUM_PORT', '8080')

accesslog = '-'
access_log_format = '%a %l %u %t "%r" %s %b "%{Referrer}i" "%{User-Agent}i" %Tf'

search_api_log = '-'
search_api_log_format = '%a %l %u %t "%r" %s %b "%{Referrer}i" "%{User-Agent}i" %Tf'

bind = ['0.0.0.0:{}'.format(port)]
workers = 4 if production else 1
worker_class = 'aiohttp.worker.GunicornWebWorker'
reload = not production

del production
