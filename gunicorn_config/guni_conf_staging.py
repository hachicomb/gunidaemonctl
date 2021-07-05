proc_name = 'guni_conf_staging' # The proc name must be set to the same value as the filename of gunicorn config.
pythonpath = './'
wsgi_app = 'main_fast_api:app'
workers = 2
worker_class = 'uvicorn.workers.UvicornWorker'
bind = '127.0.0.1:1080'
raw_env = ['MODE=PROD']
daemon = True
pidfile = './logs/staging_prod.pid'
errorlog = './logs/staging_error_log.txt'
accesslog = './logs/staging_access_log.txt'
loglevel = 'info'
capture_output = True
