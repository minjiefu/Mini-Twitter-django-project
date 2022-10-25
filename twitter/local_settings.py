# checkout https://www.neilwithdata.com/django-sql-logging
import os

LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
}

AWS_ACCESS_KEY_ID = 'AKIAWF6WQU55EY3YO4H6'
AWS_SECRET_ACCESS_KEY = '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'