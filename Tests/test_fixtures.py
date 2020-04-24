import pandas as pd
import pytest

from Tests.conftest import passdictdata


#@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("passexceldata")
@pytest.mark.skip
class TestFixture:
    def test_ddt(self,passexceldata):
        print(passexceldata["username"])
        print(passexceldata["password"])
        print("testing the passdictdata fixture")
