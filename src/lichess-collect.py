import requests, time

TOURNAMENTS = ["qOuXu5XQ","RFD0ylGd","mvHPAYHc", "jqxM88Wl"]

for tid in TOURNAMENTS:
    url = f"https://lichess.org/api/tournament/{tid}/games"
    params = {"clocks": "true", "evals": "true", "opening": "true"}
    headers = {"Accept": "application/x-ndjson"}
    r = requests.get(url, params=params, headers=headers)
    with open(f"raw-data/{tid}.ndjson", "w") as f:
        f.write(r.text)
    print(tid, r.status_code, len(r.text.splitlines()), "games")
    time.sleep(2)