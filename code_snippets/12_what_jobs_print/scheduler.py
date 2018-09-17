def submit(jobs):
    for job in jobs:
        print(type(job).__name__)
        print([
            name for name in dir(job)
            if not name.startswith("__")
        ])
        try:
            submit_job(job, priority=job.meta.priority)
            log(job.name, success=True)
        except queue.Full:
            log(job.name, success=False)
