# 0x10. Python - Network #0

# About
HTTP Protocol:
* Versions
* Request methods
* Format - Headers and Body
* Cookies
* Using `curl`

# Tasks
1. Script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
	* [0-body_size.sh](0-body_size.sh)
2. Script that akes in a URL, sends a `GET` request to the URL, and displays the body of the response
	* [1-body.sh](1-body.sh)
3. Script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
	* [2-delete.sh](2-delete.sh)
3. Script that takes in a URL and displays all HTTP methods the server will accept.
	* [3-methods.sh](3-methods.sh)
4. Script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
	* [4-header.sh](4-header.sh)
5. Script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
	* [5-post_params.sh](5-post_params.sh)
6. Write a function that finds a peak in a list of unsorted integers.
	* Prototype: `def find_peak(list_of_integers):`
	* [6-peak.py](6-peak.py) contains the function
	* [6-peak.txt](6-peak.txt) contains the complexity of your algorithm
	* **Note:** there may be more than one peak in the list
7. Script that sends a request to a URL passed as an argument, and displays only the status code of the response.
	* [100-status_code.sh](100-status_code.sh)
8. Script that sends a JSON `POST` request to a URL passed as the first argument, and displays the body of the response.
	* [101-post_json.sh](101-post_json.sh)
9. Script that makes a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing `You got me!`, in the body of the response.
	* [102-catch_me.sh](102-catch_me.sh)
