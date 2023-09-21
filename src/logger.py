import logging
import datetime
import os

# Define color codes for different log levels
COLORS = {
    'DEBUG': '\033[94m',   # Blue
    'INFO': '\033[92m',    # Green
    'WARNING': '\033[93m',  # Yellow
    'ERROR': '\033[91m',   # Red
    'CRITICAL': '\033[91m' + '\033[1m',  # Bold Red
}
RESET = '\033[0m'  # Reset color

def cleanup_logs(log_dir: str = 'logs'):
    # Remove the latest.log file
    latest_log_file_path = os.path.join(log_dir, 'latest.log')
    if os.path.exists(latest_log_file_path):
        os.remove(latest_log_file_path)

def create_logger(logger_name: str, log_dir: str = 'logs'):
    # Create log directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create file handlers
    log_file_name = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.log'
    log_file_path = os.path.join(log_dir, log_file_name)
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.INFO)

    latest_log_file_path = os.path.join(log_dir, 'latest.log')
    latest_file_handler = logging.FileHandler(latest_log_file_path)
    latest_file_handler.setLevel(logging.INFO)

    # Create a custom log formatter
    class ColoredFormatter(logging.Formatter):
        def format(self, record):
            log_message = super(ColoredFormatter, self).format(record)
            log_level = record.levelname

            # Apply color only to the log level
            log_level_colored = COLORS.get(log_level, '') + log_level + RESET

            # Replace the original log level with the colored one
            log_message = log_message.replace(log_level, log_level_colored, 1)

            return log_message

    # Create formatter
    console_format = '[{asctime}] - {levelname:^8} - [{name}]: {message}'
    console_formatter = ColoredFormatter(console_format, style='{')

    file_format = '[{asctime}] - {levelname:^8} - [{name}]: {message}'
    file_formatter = logging.Formatter(file_format, style='{')

    # Add formatter to handlers
    console_handler.setFormatter(console_formatter)
    file_handler.setFormatter(file_formatter)
    latest_file_handler.setFormatter(file_formatter)

    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.addHandler(latest_file_handler)

    return logger
