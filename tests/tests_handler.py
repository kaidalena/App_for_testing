import deepdiff, json


def compare(pattern, current_result):
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
                    ok, res = compare(pat, cur)
    return (failed_result == set()) or ok, comparison_result if res == {} else res