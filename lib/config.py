import configparser


class ConfigReader:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("./config.ini")
        self.browser_name = self._get_browser_name()
        self.repo_path = self.config["GIT_REPO"]["location"]

    def _get_browser_name(self):
        if "BROWSER" not in self.config:
            return None
        elif "browser_name" not in self.config["BROWSER"]:
            return ""
        else:
            return self.config["BROWSER"]["browser_name"]
