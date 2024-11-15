def http_request(status):
    match status:
        case 200:
            return 'HTTP/1.1 200 OK'
        case 301:
            return 'HTTP/1.1 301 Moved Permanently'
        case 404:
            return 'HTTP/1.1 404 Not Found'
        case 500:
            return 'HTTP/1.1 500 Internal Server Error'
        case status:
            return f'HTTP/1.1 {status} Unknown Status'
        
status = int(input("Enter a status code :"))
print(http_request(status))