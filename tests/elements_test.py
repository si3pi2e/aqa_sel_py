import time
from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver=driver, url='https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.check_fill_form()
            time.sleep(3)
            assert full_name == output_full_name, "the full name does not match."
            assert email == output_email, "the email does not match."
            assert current_address == output_current_address, "the current address does not match."
            assert permanent_address == output_permanent_address, "the permanent address does not match."
