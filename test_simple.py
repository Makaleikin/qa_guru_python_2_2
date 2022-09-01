from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture()
def browser_open_and_set_size():
    browser.config.window_width = 1600
    browser.config.window_height = 900
    browser.open('https://www.google.com/ncr')
    yield


def test_google_found_selene_positive(browser_open_and_set_size):
    browser.element('[name = "q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id = "search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_not_found_selezen_negative(browser_open_and_set_size):
    browser.element('[name = "q"]').should(be.blank).type('selezen').press_enter()
    browser.element('[id = "search"]').should(have.no.text('Selene - User-oriented Web UI browser tests in Python'))
