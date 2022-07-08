from selenium import webdriver

from package import write_data, get_url_website_with_google, get_url_website_with_bing, \
    get_url_website_with_yahoo, get_url_website_with_yandex, get_url_website_with_duckduckgo, \
    get_url_website_with_aol, get_url_website_with_ecosia, get_url_website_with_baidu

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
# to supress the error messages/logs
options.add_experimental_option('excludeSwitches', ['enable-logging'])

timkiem = input("\nEnter keywords: ")

URL_all = []

try:
    URLs_google = get_url_website_with_google(options, timkiem)
    URLs_bing = get_url_website_with_bing(options, timkiem)
    URLs_yahoo = get_url_website_with_yahoo(options, timkiem)
    URLs_yandex = get_url_website_with_yandex(options, timkiem)
    URLs_duckduckgo = get_url_website_with_duckduckgo(options, timkiem)
    URLs_aol = get_url_website_with_aol(options, timkiem)
    # URLs_baidu = get_url_website_with_baidu(options, timkiem)

    URL_all = URL_all + URLs_google
    URL_all = URL_all + URLs_yahoo
    URL_all = URL_all + URLs_bing
    URL_all = URL_all + URLs_duckduckgo
    URL_all = URL_all + URLs_aol
    URL_all = URL_all + URLs_yandex
    # URL_all = URL_all + URLs_baidu

    # URL_all = URL_all + URLs_bing + URLs_google + URLs_yahoo

    write_data(timkiem, URL_all)

except Exception as e:
    print(e)
