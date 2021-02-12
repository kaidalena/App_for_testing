import json


class MyQuery():
    def __init__(self):
        self.query_obj = {
            "url": '',
            "method": '',
            "params": {
                "query": {},
                "path": {},
                "saved_before": {
                    "path": [],
                    "query": []
                }
            },
            "custom_headers": {
                "saved_before": [],
                "headers": {}
            },
            "request_body_json": {},
            "commands_before_running": {},
            "checks": {
                "in_body": {},
                "in_code": {},
                "in_message": {}
            },
            "saves_from_body": []
        }

    def set_url(self, url):
        self.query_obj['url'] = url

    def set_method(self, method):
        self.query_obj['method'] = method

    def add_path_params(self, path_params={}):
        for key, val in path_params.items():
            self.query_obj['params']['path'][key] = val

    def add_query_params(self, query_params={}):
        for key, val in query_params.items():
            self.query_obj['params']['query'][key] = val

    def add_path_params_saved_before(self, path_params=[]):
        self.query_obj['params']['saved_before']['path'] += path_params

    def add_query_params_saved_before(self, query_params=[]):
        self.query_obj['params']['saved_before']['query'] += query_params

    def add_headers(self, headers={}):
        for key, val in headers.items():
            self.query_obj['custom_headers']['headers'][key] = val

    def add_headers_saved_before(self, headers=[]):
        self.query_obj['custom_headers']['saved_before'] += headers

    def set_request_body(self, json_data={}):
        self.query_obj['request_body_json'] = json.dumps(json_data)

    def set_checks(self, area='body', json_data={}):
        in_area = f'in_{area}'
        self.query_obj['checks'][in_area] = json_data

    def add_params_save_from_response(self, params_to_save=[]):
        self.query_obj['saves_from_body'] += params_to_save

    def get_query(self):
        return self.query_obj