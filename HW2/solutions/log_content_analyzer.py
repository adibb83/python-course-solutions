
def analyze_log_content(log :str) -> dict:
    log_dictionary = dict(Error=0, Warning=0, Info=0)
    words_in_string = log.split()

    for word in words_in_string:
        if word.capitalize() in log_dictionary:
            log_dictionary[word.capitalize()] += 1
    return log_dictionary


log_content = """
2024-04-29 15:45:00,089 INFO [name:starwars_engine][pid:2995] Message one
2024-04-29 15:45:05,123 WARNING [name:starwars_engine][pid:2996] Check disk space
2024-04-29 15:45:08,111 /var/log/apache2/server.access.log 172.18.0.12 - - "POST /api/command/?201dfd68-e48d-587b-e715-3ff83ef3af19 HTTP/1.1" 200
2024-04-29 15:45:10,456 ERROR [name:starwars_engine][pid:2997] Failed to start engine
2024-04-29 15:46:00,789 INFO [name:starwars_engine][pid:2998] All systems go
"""

print(analyze_log_content(log_content))
