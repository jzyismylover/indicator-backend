import os
from yaml import safe_load

def init_enviro():
    FILE_NAME = os.path.join('config', 'config.yml')
    with open(FILE_NAME, 'rb') as f:
        try:
            if os.path.exists('/.dockerenv'):
                _config_prefix = 'pd_'
            else:
                _config_prefix = 'de_'
            _config = safe_load(f)
            _db_config = _config[_config_prefix + 'db']
            _redis_config = _config[_config_prefix + 'redis']
            _celery_confg = _config[_config_prefix + 'celery']
            _mail_config = _config['mail']
            set_configuration('db', _db_config)
            set_configuration('redis', _redis_config)
            set_configuration('celery', _celery_confg)
            set_configuration('mail', _mail_config)
        except:
            pass


def set_configuration(prefix: str, config: dict):
    prefix = prefix.upper()
    for key in config.keys():
        val = config[key]
        key = f'{prefix}_{key.upper()}'
        os.environ[key] = str(val)

init_enviro()
# os.environ['HANLP_LOAD'] = 'True'

from config.db import init_db
from config.redis import init_redis, mark_dyn_data, get_dyn_data
from config.mail import init_mail
from config._celery import init_celery
from config._schedule import init_scheduler
