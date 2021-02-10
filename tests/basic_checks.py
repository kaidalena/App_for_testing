def check_mimetype(mimetype, correct_mimetype='application/json;  charset=utf-8'):
    assert mimetype == correct_mimetype, f'Received response mimetype "{mimetype}", but it should have been "{correct_mimetype}"'


def check_http_code(code, correct_code=200):
    assert code == correct_code, f'Http code {code} was received, but it should have been {correct_code}'


def check_structure_successful_response(response):
    assert isinstance(response, dict), 'Response does not belong to the json type'
    assert {'body', 'code', 'message'}.issubset(response.keys()), 'Response does not match the structure {body, code, message}'
    assert response['code'] is None, "'Code' contains an error code"
    assert response['message'] is None, "'Message' contains a message"
    assert response['body'] is not None, 'Body should not be empty'