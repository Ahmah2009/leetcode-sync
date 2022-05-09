import browser_cookie3
from lib.errors import BrowserNotSupported


def load_cookies_jar(browser="chrome", host="leetcode.com"):
    browsers = {
        "chrome": browser_cookie3.chrome,
        "firefox": browser_cookie3.firefox,
        "brave": browser_cookie3.brave,
    }
    if browser not in browsers:
        raise BrowserNotSupported

    cookies_jar = browsers[browser](domain_name=host)
    return cookies_jar
