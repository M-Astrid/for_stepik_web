from cgi import parse_qsl

def app(env, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    qs = parse_qsl(env['QUERY_STRING'], encoding='utf-8') 

    body = ''
    for key, value in qs:
        body += key + '=' + value + '\r\n'

    start_response(status, headers)  
    return body