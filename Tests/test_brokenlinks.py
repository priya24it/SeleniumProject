import pytest

@pytest.mark.usefixtures("setup")
class TestBrokenlinks:

    def test_brokenlinks(self):
        print("finding links")
        alllinks = self.driver.find_elements_by_tag_name("a")
        for links in alllinks:
            print(links.text)
