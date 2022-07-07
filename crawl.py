from selenium import webdriver

from package.file import write_data
from package.google import get_url_website_with_google
from package.bing import get_url_website_with_bing
from package.yahoo import get_url_website_with_yahoo


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
# to supress the error messages/logs
options.add_experimental_option('excludeSwitches', ['enable-logging'])

timkiem = input("\n nhập từ khóa tìm kiếm : ")

URL_all = []

try:
    # URLs_google_one_page = get_url_website_with_google(options, timkiem)
    URLs_bing_one_page = get_url_website_with_bing(options, timkiem)
    # URLs_yahoo_one_page = get_url_website_with_yahoo(options, timkiem)
    # URL_all = URL_all + URLs_bing_one_page + URLs_google_one_page + URLs_yahoo_one_page
    # URL_all = URL_all + URLs_google_one_page
    # URL_all = URL_all + URLs_yahoo_one_page
    URL_all = URL_all + URLs_bing_one_page

    write_data(timkiem, URL_all)

except Exception as e:
    print(e)
