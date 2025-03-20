import requests

#Custom Exception Class
class ResponseException(Exception):
    def __init__(self, status, reason):
        self.status = status
        self.reason = reason
    
    def __str__(self):
        return f"Status: {self.status}, Reason: {self.reason}"


#class to handle request
class getCall:
    def __init__(self, url):
        self.url = url
    
    def request(self):
        response = requests.get(self.url)
        if not response.ok: 
            raise ResponseException(response.status_code, response.reason)
        return response


if __name__ == "__main__":
    try:
        get_obj = getCall("https://google.com/naman")
        print(get_obj.request())
    except ResponseException as e:
        print("Error in request status!", e)