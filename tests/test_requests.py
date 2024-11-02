from pathlib import Path
import sys
import requests
from requests.models import Response

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.wrapper import Request

def test_is_active_mock_get_data_200(mocker):
    """
    get_data関数の返すstatus_codeが200になるようにする。
    """
    # レスポンスオブジェクトをモック
    mock_response = Response()
    mock_response.status_code = 200
    
    # requests.getをモックして、mock_responseを返すように設定
    mocker.patch("src.wrapper.requests.get", return_value=mock_response)

    # テスト実行
    url = "https://www.google.com"
    assert Request(url).get_data().status_code == 200

def test_is_active_mock_get_data_404(mocker):
    """
    get_data関数の返すstatus_codeが404になるようにする。
    GoogleのURLを指定しているが、404になる場合。
    """
    # レスポンスオブジェクトをモック
    mock_response = Response()
    mock_response.status_code = 404
    
    # requests.getをモックして、mock_responseを返すように設定
    mocker.patch("src.wrapper.requests.get", return_value=mock_response)

    # テスト実行
    url = "https://www.google.com"
    assert Request(url).get_data().status_code == 404

def test_is_active_mock_get_data_url_miss_404(mocker):
    """
    get_data関数の返すstatus_codeが404になるようにする。
    URLを間違えている場合。
    """
    # レスポンスオブジェクトをモック
    mock_response = Response()
    mock_response.status_code = 404
    
    # requests.getをモックして、mock_responseを返すように設定
    mocker.patch("src.wrapper.requests.get", return_value=mock_response)

    # テスト実行
    url = "https://www.google-miss.com"
    assert Request(url).get_data().status_code == 404

def test_is_active_mock_get_data_403(mocker):
    """
    get_data関数の返すstatus_codeが403になるようにする。
    """
    # レスポンスオブジェクトをモック
    mock_response = Response()
    mock_response.status_code = 403
    
    # requests.getをモックして、mock_responseを返すように設定
    mocker.patch("src.wrapper.requests.get", return_value=mock_response)

    # テスト実行
    url = "https://www.google.com"
    assert Request(url).get_data().status_code == 403
