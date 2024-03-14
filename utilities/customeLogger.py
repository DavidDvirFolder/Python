import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        # Ensure the "Logs" directory exists
        logs_dir = "Logs"
        os.makedirs(logs_dir, exist_ok=True)

        # Get the logger with the name of the current module
        logger = logging.getLogger(__name__)

        # Avoid duplicate handlers
        if not logger.handlers:
            # Create a formatter with the specified log message format and date format
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                                          datefmt='%m/%d/%Y %I:%M:%S %p')

            # Create a file handler for writing log messages to a file
            file_handler = logging.FileHandler(os.path.join(logs_dir, "automation.log"))

            # Set the formatter for the file handler
            file_handler.setFormatter(formatter)

            # Add the file handler to the logger
            logger.addHandler(file_handler)

            # Set the logging level for the logger
            logger.setLevel(logging.INFO)

        # Return the configured logger
        return logger
