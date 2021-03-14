import os
from config import config

LOGGING_CONFIG = {
    "version": 1,
    "loggers": {
        "": {
            "level": "NOTSET",
            "handlers": [
                "debug_console_handler",
                "info_rotating_file_handler",
                "error_file_handler",
            ],
        },
        "sqlalchemy": {
            "level": "WARNING",
            "propagate": False,
            "handlers": ["info_rotating_file_handler", "error_file_handler"],
        },
        "faker": {
            "level": "WARNING",
            "propagate": False,
            "handlers": ["info_rotating_file_handler", "error_file_handler"],
        },
    },
    "formatters": {
        "info": {
            "format": "%(asctime)s-%(levelname)s-%(name)s::"
            "%(module)s|%(lineno)s:: %(message)s"
        },
        "error": {
            "format": "%(asctime)s-%(levelname)s-%(name)s-%(process)d::"
            "%(module)s|%(lineno)s:: %(message)s"
        },
    },
    "handlers": {
        "debug_console_handler": {
            "level": "DEBUG",
            "formatter": "info",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "info_rotating_file_handler": {
            "level": "INFO",
            "formatter": "info",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(config["log_folder"], "datyy_info.log"),
            "mode": "a",
            "maxBytes": 1048576,
            "backupCount": 10,
        },
        "error_file_handler": {
            "level": "WARNING",
            "formatter": "error",
            "class": "logging.FileHandler",
            "filename": os.path.join(config["log_folder"], "datyy_error.log"),
            "mode": "a",
        },
    },
}
