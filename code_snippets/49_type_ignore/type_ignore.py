

async_queue = queue.Queue()

def unblock_queue_callback() -> None:
     with async_queue.all_tasks_done:  # type: ignore
         async_queue.all_tasks_done.notify_all()  # type: ignore

timeout = MyTimeout(60, callback=unblock_queue_callback)

# wait for all async logging jobs to finish
try:
    with timeout:
        async_queue.join()
except MyTimeoutError as ex:
    log()
