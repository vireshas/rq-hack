###rq hack

Enqueuing a job from a python script.  

#####Installation
        pip install rq  
        start redis(expecting default settings)  
        rqworker  
        python enqueue_job_to_rq.py  

enqueue_job_to_rq.py: enqueues a job from python script  

Use cases:  
        1. Enqueue a job from another language  
        2. Reusing existing python codebase via rq workers and use a language specific client  
