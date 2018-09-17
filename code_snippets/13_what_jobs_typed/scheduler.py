from typing import Iterable
from fb.scheduler.jobs import Job


def submit(jobs: Iterable[Job]) -> None:
    for job in jobs:
        try:
            submit_job(job, priority=job.meta.priority)
            log(job.name, success=True)
        except queue.Full:
            log(job.name, success=False)
