# 0x11. Python - Network #1

# About
Python web packages:
* `urllib`
* `requests`
# Tasks
0. Python script that fetches https://alx-intranet.hbtn.io/status using `urllib` package.
	* [0-hbtn_status.py](0-hbtn_status.py)
1. Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response `urllib` package.
	* [1-hbtn_header.py](1-hbtn_header.py)
2. Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`) `urllib` package.
	* [2-post_email.py](2-post_email.py)
3. Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`) using `urllib` package.
	* Manages `urllib.error.HTTPError` exceptions and print: `Error code:` followed by the HTTP status code.
	* [3-error_code.py](3-error_code.py)
4. Python script that fetches https://alx-intranet.hbtn.io/status using `requests` package.
	* [4-hbtn_status.py](4-hbtn_status.py)
5. Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header using `request` package.
	* [5-hbtn_header.py](5-hbtn_header.py)
6. Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response using `requests` package.
	* [6-post_email.py](6-post_email.py)
7. Python script that takes in a URL, sends a request to the URL and displays the body of the response using `requests` package
	* If the HTTP status code is greater than or equal to 400, print: `Error code:` followed by the value of the HTTP status code.
	* [7-error_code.py](7-error_code.py)
8. Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.
	* [8-json_api.py](8-json_api.py)
9. Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your `id`.
	* [10-my_github.py](10-my_github.py)
10. ython script that takes 2 arguments: `reposistory name` and `owner name` and list 10 commits (from the most recent to olders) of the repository
	* [100-github_commits.py](100-github_commits.py)
