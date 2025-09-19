from page.home_page import Home
from page.login_page import Login
import pytest
from corelib import logger as _logger, utils
import time
from datetime import datetime, timedelta
from corelib import email_handler

logger = _logger.Logger(prefix="test_search", log_level="INFO")

@pytest.mark.download_excel_1
def test_download_excel(page, config, api):
    login = Login(page)
    download_ex = Home(page)
    login.navigate_to_login_page(base_url = config["base_url"])
    login.login_into_website(username=config["username_1"], password=config["password_1"])
    function_name = "Mode06"
    make_name = "Chrysler" 
    download_ex.search_information(make_name=make_name, function_name = function_name)
    # edit.fill_notes_box(rd_notes=rd_notes_expected, release_notes=release_notes_expected, lib_log=lib_log_expected)
    start_utc = email_handler.mark_now_utc() - timedelta(seconds=2)
    resp, data, _ = api.run_and_wait_json(
            trigger=lambda: download_ex.download_excel(),
            base_api=config["base_api"],
            path_or_url="/api/function/export-excel-data",
            method="POST",
            expected_status=200,
            timeout=30000,
        )
    excel_email = email_handler.wait_for_excel_email(
    imap_server=config["imap_server"],
    imap_port=int(config.get("imap_port", 993)),
    username=config["imap_user"],
    password=config["imap_password"],
    sender_filter="innovaserver@vn.innova.com",
    cutoff_dt_utc=start_utc,
    subject_keyword="Excel",
    delivery_wait=8,   # chờ lần đầu 8s cho mail tới
    timeout=240,
    interval=10,
    )


    
    logger.info(f"email full: {excel_email}")
    utils.download_file(excel_email["download_url"], "downloaded_excel.zip")
    
    # assert "Excel" in mail["subject"]
    # logger.info(f"email: {mail['subject']} | from={mail['from']} | at={mail['date_dt_utc']}")
    # assert "excel" in mail["subject"].lower()
    # assert mail.get("download_link"), "Không tìm thấy link trong email"
    
    


    # delete.reload_page()
    # time.sleep(2)

    # assert ui
    # rd_notes_section = edit.get_sections_pro_db_info(section="rd_note")
    # assert rd_notes_section["R&D Note"] == rd_notes_expected

    # release_notes_section = edit.get_sections_pro_db_info(section="release_note")
    # assert release_notes_section["Release Note"] == release_notes_expected
    
    # lib_log_section = edit.get_sections_pro_db_info(section="lib_log")
    # assert lib_log_section["Lib Log"] == lib_log_expected

@pytest.mark.download_excel
def test_download_excel_btn_visibility(page, config):
    login = Login(page)
    download_ex = Home(page)
    login.navigate_to_login_page(base_url = config["base_url"])
    login.login_into_website(username=config["username"], password=config["password"])
    feature = "Common"
    make_name = "Honda"
    download_ex.search_information(make_name=make_name, function_name = feature)
    # if download_ex.is_draft_existing:
        # verify ui -> "download excel" display?
        # download_ex.download_excel()
    # else:

@pytest.mark.download_excel
def test_download_excel_cancel(page, config):
    login = Login(page)
    download_ex = Home(page)
    login.navigate_to_login_page(base_url = config["base_url"])
    login.login_into_website(username=config["username"], password=config["password"])
    feature = "Common"
    make_name = "Honda"
    download_ex.search_information(make_name=make_name, function_name = feature)
    # if download_ex.is_draft_existing:
        # verify ui -> "download excel" display?
        # download_ex.download_excel()
    # else:

