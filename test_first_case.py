import basic_checks as checks, http_query
from tests_handler import generate_uuid_v1
import deepdiff, json
from __init__ import logger
import time


def sleep(seconds):
    time.sleep(seconds)


supported_commands = {
    'sleep': {
        'func': sleep,
        'params': ['seconds']
    }
}


def compare_result(pattern, current_result):
    not_allowed_values = list(["values_changed", "dictionary_item_removed", "type_changes"])
    diff = deepdiff.DeepDiff(pattern, current_result)
    comparison_result = json.loads(diff.to_json())
    result_keys = set(comparison_result.keys())
    failed_result = set(not_allowed_values).intersection(result_keys)

    ok = False
    res = {}
    if failed_result != set() and 'iterable_item_added' in comparison_result.keys():
        if isinstance(pattern, list) and isinstance(current_result, list):
            for pat in pattern:
                for cur in current_result:
                    ok, res = compare_result(pat, cur)
    return (failed_result == set()) or ok, comparison_result if res == {} else res


def test_second():
    global supported_commands
    try:
        tests_file_path = './tests_descriptions.json'
        logger.info(f'---------------------- run test {tests_file_path} ----------------------')
        saved_values = {}
        test_data = {}
        with open(tests_file_path, 'r', encoding='utf-8') as file:
            test_data = json.load(file)

        for query in test_data:
            if query['commands_before_running'] != {}:
                logger.info(f"commands_before_running: {query['commands_before_running']}")
                for command in query['commands_before_running']:
                    logger.info(f"run: {query['commands_before_running']}{query['commands_before_running'][command]}")
                    supported_commands[command]['func'](**(query['commands_before_running'][command]))


            if 'saved_before' in query['params'].keys():
                for type_param, array_name_params in query['params']['saved_before'].items():
                    for name in array_name_params:
                        query['params'][type_param][name] = saved_values[name]

            if 'saved_before' in query['custom_headers'].keys():
                for name_header in query['custom_headers']['saved_before']:
                    query['custom_headers']['headers'][name_header] = saved_values[name_header]

            print(f"params: {query['params']}")
            print(f"custom_headers: {query['custom_headers']}")

            url = str(query['url']).format(**query['params']['path'])
            response = http_query.http_query_by_type[str(query['method']).lower()](
                url=url,
                headers=query['custom_headers']['headers'],
                query_params=query['params']['query'],
                json_data=query['request_body_json'],
            )
            # checks.check_mimetype(mimetype=response.content_type)
            checks.check_mimetype(mimetype=response.headers['content-type'])
            checks.check_http_code(code=response.status_code)
            response_data_json = response.json()
            checks.check_structure_successful_response(response=response_data_json)
            for scan_area, pattern in query['checks'].items():
                if pattern is not None:
                    area = str(scan_area).replace('in_', '')
                    ok, res_comparison = compare_result(pattern, response_data_json[area])

                    assert ok is True, f'A result that does not match the pattern was found.\nResult of comparing the url [{url}] response:\n{res_comparison}'

            for param_for_save in query['saves_from_body']:
                saved_values[param_for_save] = response_data_json['body'][param_for_save]
    except AssertionError as ex:
        logger.error(ex)
        print(f'[Error]{ex}')

test_second()