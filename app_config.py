class AppConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppConfig, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        # Initialize configuration settings
        self.settings = {
            "theme": "light",
            "language": "en",
            "timeout": 30
        }

    def get_setting(self, key):
        return self.settings.get(key, None)

    def set_setting(self, key, value):
        self.settings[key] = value

# Usage
config1 = AppConfig()
config2 = AppConfig()

# Accessing settings via different instances
print(config1.get_setting("theme"))  # Output: light
print(config2.get_setting("language"))  # Output: en

# Updating a setting via one instance
config1.set_setting("timeout", 60)

# Reflects in the other instance as well
print(config2.get_setting("timeout"))  # Output: 60

# Check if both config1 and config2 are the same instance
print(config1 is config2)  # Output: True
