from pages.login_page import LoginPage


def test_valid_login(page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert "inventory" in page.url


def test_invalid_username(page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        "wrong_user",
        "secret_sauce"
    )

    error_message = page.locator(
        "[data-test='error']"
    ).inner_text()

    assert "Username and password do not match" in error_message


def test_invalid_password(page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        "standard_user",
        "wrong_password"
    )

    error_message = page.locator(
        "[data-test='error']"
    ).inner_text()

    assert "Username and password do not match" in error_message


def test_empty_username(page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        "",
        "secret_sauce"
    )

    error_message = page.locator(
        "[data-test='error']"
    ).inner_text()

    assert "Username is required" in error_message


def test_empty_password(page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        "standard_user",
        ""
    )

    error_message = page.locator(
        "[data-test='error']"
    ).inner_text()

    assert "Password is required" in error_message