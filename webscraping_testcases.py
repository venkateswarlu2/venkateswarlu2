import pytest
from unittest.mock import patch, MagicMock
import requests

import webscraping_multithreading  # Replace with the actual script name

def test_scrape_website_success(mocker):
    """Tests successful scraping of a website with expected data."""

    # Mock requests.get to return a successful response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.content = b'<!DOCTYPE html><html><head><title>Test Title</title></head><body><h1>Test Heading</h1></body></html>'
    mocker.patch('requests.get', return_value=mock_response)

    # Mock BeautifulSoup to find the expected element
    mock_soup = MagicMock()
    mock_soup.find_all.return_value = [MagicMock(text='Test Heading')]
    mocker.patch('bs4.BeautifulSoup', return_value=mock_soup)

    # Simulate successful CSV writing (no need to actually write)
    with patch('csv.writer') as mock_writer:
        webscraping_multithreading.scrape_website('https://example.com')

    # Assert logging messages
    assert webscraping_multithreading.logger.info.call_count == 2  # One for scraping, one for completion
    assert webscraping_multithreading.logger.info.call_args_list[0][0][0] == "Scraped heading: Test Heading from https://example.com"
    assert webscraping_multithreading.logger.info.call_args_list[1][0][0] == "Scraping completed. See scraping.log for details."

def test_scrape_website_no_headings(mocker):
    """Tests scraping a website with no heading elements."""

    # Mock requests and BeautifulSoup as before
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.content = b'<!DOCTYPE html><html><body></body></html>'
    mocker.patch('requests.get', return_value=mock_response)
    mock_soup = MagicMock()
    mock_soup.find_all.return_value = []
    mocker.patch('bs4.BeautifulSoup', return_value=mock_soup)

    # Simulate successful CSV writing (no need to actually write)
    with patch('csv.writer') as mock_writer:
        webscraping_multithreading.scrape_website('https://example.com')

    # Assert logging messages
    assert webscraping_multithreading.logger.info.call_count == 1  # Only completion message
    assert webscraping_multithreading.logger.warning.call_count == 1
    assert webscraping_multithreading.logger.warning.call_args[0][0] == "No heading elements (h1, h2, h3) found on https://example.com"

def test_scrape_website_request_error(mocker):
    """Tests scraping with a request exception."""

    # Mock requests to raise an exception
    mocker.patch('requests.get', side_effect=requests.exceptions.RequestException('Simulated error'))

    # No need to mock BeautifulSoup or CSV writer as scraping won't proceed

    with pytest.raises(requests.exceptions.RequestException):
        webscraping_multithreading.scrape_website('https://example.com')

    # Assert logging message
    assert webscraping_multithreading.logger.error.call_count == 1
    assert webscraping_multithreading.logger.error.call_args[0][0] == "Error fetching https://example.com: Simulated error"

