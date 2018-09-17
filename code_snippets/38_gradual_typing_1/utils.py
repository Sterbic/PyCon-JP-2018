# utils.py
import json


def pretty_print(job: Job) -> None:
    print(json.dumps(job, indent=4))
