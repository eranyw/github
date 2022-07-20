import pytest
import logging

def testlogin():
    print("login sucessfual")

def testlogoff():
        print("logoff sucessfual")


def testcalculiotn ():
    assert 2+2 == 4

LOGGER = logging.getLogger(__name__)


def test_log():
    LOGGER.info('info')
    LOGGER.warning('warning')
    LOGGER.error(' error')
    LOGGER.critical('critical')
    assert True
