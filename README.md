###rq(https://github.com/nvie/rq) hack

Enqueuing a job from a python script.  

#####Installation
        pip install rq  
        start redis(expecting default settings)  
        rqworker  
        python enqueue_job_to_rq.py  

<b>enqueue_job_to_rq.py: enqueues a job from python script</b>  

######Using golang client to enqueue a job
        from the cloned directory, cd go-client  
        go run main.go
        
Use cases:  
        1. Enqueue a job from another language  
        2. Reusing existing python codebase via rq workers and enqueue a job from any language    
