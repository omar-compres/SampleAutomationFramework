
class Utils:

    @staticmethod
    def is_text_equal(expected_text, actual_text):
        if expected_text != actual_text:
            print("\nExpected: " + expected_text + "\nActual: " + actual_text)
            return False
        return True
