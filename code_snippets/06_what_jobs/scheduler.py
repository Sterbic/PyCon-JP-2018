def submit(jobs):
    for job in jobs:
        try:
            submit_job(job, priority=job.meta.priority)
            log(job.name, success=True)
        except queue.Full:
            log(job.name, success=False)
