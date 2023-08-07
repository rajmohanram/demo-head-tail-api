wsgi_app = 'wsgi:app'
accesslog = '-'
errorlog = '-'
loglevel = 'info'
bind = "0.0.0.0:8001"
workers = 4
worker_class = "sync"
timeout = 600
