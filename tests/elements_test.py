import time
from pages.elements_page import TextBoxPage, CheckBoxPage


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

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, url='https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()

            time.sleep(1)
            input_check_box = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()

            assert input_check_box == output_result, "choice checkboxes have not been selected"