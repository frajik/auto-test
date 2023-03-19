import requests
import pprint


class TestJoke():
    """Создание шутки"""

    def __init__(self):
        pass

    def create_new_joke(self):

        url = "https://api.chucknorris.io/jokes/random"
        print(url)
        result = requests.get(url)
        print(result.text)
        print("status code: " + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Successfully")
        else:
            print("Error")
        result.encoding = "utf-8"
        print()
        pprint.pprint(result.text)
        check = result.json()
        # check_info = check.get("categories")
        # print(check_info)
        # assert check_info == []
        # print("Successfully")
        check_info_value = check.get("value")
        print(check_info_value)
        if "Chuck" in check_info_value:
            print("Successfully")
        else:
            print("something's wrong.")


random_joke = TestJoke()
random_joke.create_new_joke()
