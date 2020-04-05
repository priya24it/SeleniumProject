import pytest

from UtilityClass.utilityclass import commonclass

class Test2(commonclass):

    @pytest.mark.smoke
    def test_smoke1(self):
        global log
        log = self.getLogger()
        log.info("smoke testing1")

    @pytest.mark.regression
    def test_regression1(self):
        log.info("regression testing1")

    @pytest.mark.smoke
    def test_smoke2(self):
        log.info("smoke testing2")

    @pytest.mark.regression
    def test_regression2(self):
        log.info("regression testing2")

    @pytest.mark.usefixtures("passdata")
    def test_fixture(self, passdata):
        log.info(passdata)
