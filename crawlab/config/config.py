import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 爬虫源码路径
PROJECT_SOURCE_FILE_FOLDER = os.path.join(BASE_DIR, "spiders")

# 爬虫部署路径
PROJECT_DEPLOY_FILE_FOLDER = '/var/crawlab'

# 爬虫日志路径
PROJECT_LOGS_FOLDER = '/var/log/crawlab'

# 打包临时文件夹
PROJECT_TMP_FOLDER = '/tmp'

# Celery中间者URL
BROKER_URL = 'redis://127.0.0.1:6379/0'

# Celery后台URL
CELERY_RESULT_BACKEND = 'mongodb://127.0.0.1:27017/'

# Celery MongoDB设置
CELERY_MONGODB_BACKEND_SETTINGS = {
    'database': 'crawlab_test',
    'taskmeta_collection': 'tasks_celery',
}

# Celery时区
CELERY_TIMEZONE = 'Asia/Shanghai'

# 是否启用UTC
CELERY_ENABLE_UTC = True

# flower variables
FLOWER_API_ENDPOINT = 'http://localhost:5555/api'

# MongoDB 变量
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DB = 'crawlab_test'

# Flask 变量
DEBUG = False
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 8000