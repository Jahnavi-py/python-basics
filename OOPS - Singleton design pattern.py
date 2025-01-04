#Implement a Logger class using the Singleton design pattern.
class Logger:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._log_file = "app.log"
            cls._instance._log_level = "INFO"
        return cls._instance
    def log(self, message):
        with open(self._log_file, "a") as file:
            file.write(f"[{self._log_level}] {message}\n")
        print(f"[{self._log_level}] {message}")
    def set_log_level(self, level):
        self._log_level = level
logger1 = Logger()
logger1.log("This is an info message.")
logger1.set_log_level("ERROR")
logger1.log("This is an error message.")
logger2 = Logger()
print(logger1 is logger2)