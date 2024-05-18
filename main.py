class SingletonLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonLogger, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        # This method will be called only once
        self.log_file = open('app.log', 'a')

    def log(self, message):
        self.log_file.write(f'{message}\n')
        self.log_file.flush()

# Usage
logger1 = SingletonLogger()
logger2 = SingletonLogger()

logger1.log("This is a log message from logger1.")
logger2.log("This is a log message from logger2.")

# Checking if both logger1 and logger2 are actually the same instance
print(logger1 is logger2)  # Output: True



# Explanation:
# __new__ method:

# This method is responsible for creating a new instance of the class. We override it to control the instantiation process.
# The first time SingletonLogger is instantiated, _instance is None, so a new instance is created, and initialize() is called to set up the logger.
# On subsequent instantiations, _instance is not None, so the existing instance is returned.
# initialize method:

# This method is used to initialize any necessary attributes. It ensures that the setup is done only once, when the instance is created for the first time.
# log method:

# This method writes log messages to the log file. Since there's only one instance of SingletonLogger, all log messages from different parts of the application will go to the same log file.
# Usage:

# When logger1 and logger2 are created, they both refer to the same instance of SingletonLogger.
# The print(logger1 is logger2) statement confirms that logger1 and logger2 are indeed the same instance.
# This simple example illustrates how the Singleton Pattern ensures that only one instance of SingletonLogger exists and is used across the entire application.
