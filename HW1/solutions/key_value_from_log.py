import re


def extract_value_from_log(log_line, key):
    pattern = rf"{key}:([^\]\[]+)"
    match = re.search(pattern, log_line)
    return match.group(1).strip()


log_line = ("2024-04-29 15:45:00,089 INFO [name:starwars_engine.spaceship_manager.tasks][pid:2995]["
            "uuid:20ebf460-dcdf-4b1f-abf1-7517ef3f63c2][process:run_services_if_needed_wrapper]["
            "function:run_services_if_needed][account:519][GamePlay:400004380] GamePlay's version is at least 'new' ("
            "5.2.0).")
key_to_find = "account"
value = extract_value_from_log(log_line, key_to_find)
print(f"The value for key '{key_to_find}' is: '{value}'")
