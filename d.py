from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class LoggingWithLogger(Logger):
    def log(self, message):
        import logging
        logging.basicConfig(level=logging.INFO)
        logging.info(message)

class LoggingWithPrint(Logger):
    def log(self, message):
        print(f"[INFO] {message}")

class Application:
    def __init__(self, logger):
        self.logger = logger

    def do_something(self):
        self.logger.log("Doing something...")

def main():
    logger = LoggingWithLogger()
    app = Application(logger)
    app.do_something()


    another_logger = LoggingWithPrint()
    app_with_another_logger = Application(another_logger)
    app_with_another_logger.do_something()

if __name__ == "__main__":
    main()
