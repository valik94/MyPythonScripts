def get_index(api_key):
    if str(api_key)!=the_api_key:
    return 401
    base_url = 'www.google.com'
    browser = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver", log_path="/path/to/geckodriver.log")
    browser.get(base_url)
    html = browser.page_source
    return html         
