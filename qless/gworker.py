#! /usr/bin/env python

import os
from qless import worker, logger

class Worker(worker.Worker):
    def __init__(self, *args, **kwargs):
        self.pool_size = kwargs.pop('pool_size', 10)
        worker.Worker.__init__(self, *args, **kwargs)
    
    def work(self):
        if not os.path.isdir(self.sandbox):
            os.makedirs(self.sandbox)
        
        from gevent.pool import Pool
        from gevent import sleep, Greenlet
        pool = Pool(self.pool_size)
        while True:
            try:
                seen = False
                for queue in self.queues:
                    # Wait until a greenlet is available
                    pool.wait_available()
                    job = queue.pop()
                    if job:
                        seen = True
                        pool.start(Greenlet(job.process))
                
                if not seen:
                    logger.debug('Sleeping for %fs' % self.interval)
                    sleep(self.interval)
            except KeyboardInterrupt:
                return
