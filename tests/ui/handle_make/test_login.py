# tests/test_example.py
from page.login_page import Login
from playwright.sync_api import expect
import time




def test_login_with_valid_account(page, config):
    login = Login(page)
    login.navigate_to_login_page(base_url = config["base_url"])
    login.login_into_website(username=config["username"], password=config["password"])
    # time.sleep(10)
    expect(page).to_have_url("https://webimporter.innovavietnam.com/", timeout = 10000)


def test_login_with_empty_username_password(page, config):
    login = Login(page)
    login.navigate_to_login_page(base_url = config["base_url"])
    login.login_into_website(username="", password="")
    # assert

def test_login_with_empty_password(page, config):
    login = Login(page)
    login.navigate_to_login_page(base_url = config["base_url"])
    login.login_into_website(username=config["username"], password="")
    # assert

def test_login_with_empty_username(page, config):
    login = Login(page)
    login.navigate_to_login_page(base_url = config["base_url"])
    login.login_into_website(username="", password=config["password"])
    # assert
def test_login_with_wrong_password(page, config):
    login = Login(page)
    login.navigate_to_login_page(base_url = config["base_url"])
    login.login_into_website(username=config["username"], password="1234")
    # assert

def test_login_with_wrong_username(page, config):
    login = Login(page)
    login.navigate_to_login_page(base_url = config["base_url"])
    login.login_into_website(username="duy.tr", password=config["password"])
    # assert

def test_login_toggle_eye_icon(page, config):
    login = Login(page)
    login.navigate_to_login_page(base_url = config["base_url"])
    # login.toggle_eye_icon()
    # login.login_into_website(username="duy.tr", password=config["password"])
    # assert

def test_login_password_invisibility_when_typing(page, config):
    login = Login(page)
    login.navigate_to_login_page(base_url = config["base_url"])
    # login.toggle_eye_icon()
    # login.login_into_website(username="duy.tr", password=config["password"])
    # assert

def test_login_forgot_password_link(page, config):
    login = Login(page)
    login.navigate_to_login_page(base_url = config["base_url"])
    # login.toggle_eye_icon()
    # login.login_into_website(username="duy.tr", password=config["password"])
    # assert
    
    
    

