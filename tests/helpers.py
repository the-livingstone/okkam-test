

def get_json(resp, status_code=200) -> dict:
    assert (
        resp.status_code == status_code
    ), f"Unexpected response: {resp.status_code} {resp.text}"
    return resp.json()
