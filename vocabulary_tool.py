import urllib
from urllib.parse import urljoin

import requests
from langchain_core.tools import tool
from requests import Response

URL = "https://c0ouez95i5.execute-api.us-west-2.amazonaws.com/daily-dragon/vocabulary"


@tool
def get_words() -> Response:
    """
    Retrieve user's list of words from vocabulary.
    :return: List of words
    """
    response = requests.get(URL).json()
    print(f"Retrieved {len(response)} words from vocabulary.")
    return response


@tool
def add_word(word: str) -> Response:
    """
    Add a word to vocabulary.
    :param word: Word to add
    :return: Response
    """
    response = requests.post(URL, json={"word": word}).json()
    print(response)
    return response


@tool
def remove_word(word: str) -> Response:
    """
    Remove a word from vocabulary.
    :param word: String word to remove.
    :return: Deletion response
    """
    encoded_word = urllib.parse.quote(word)
    delete_url = f"{URL}/{encoded_word}"
    print(f"Removing {word} from vocabulary.")
    response = requests.delete(delete_url).json()
    print(response)
    return response
