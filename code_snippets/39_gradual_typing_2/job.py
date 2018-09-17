# job.py
from utils import pretty_print


def create_job() -> Job:
    job = Job()
    pretty_print("job created!")
    return job
