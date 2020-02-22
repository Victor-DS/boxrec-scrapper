import logging


class Logger:

    def __init__(self, log_level):
        log_format_string = "%(asctime)s [%(levelname)s] %(message)s"
        log_formatter = logging.Formatter(log_format_string)
        logging.basicConfig(level=log_level, format=log_format_string)

        file_handler = logging.FileHandler("boxrec-scrapper.log")
        file_handler.setFormatter(log_formatter)
        file_handler.setLevel("DEBUG")

        log = logging.getLogger()
        log.addHandler(file_handler)

        self.log = log

    def _get_logger(self):
        return self.log

    @staticmethod
    def get_logger(log_level):
        return Logger(log_level)._get_logger()