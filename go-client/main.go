package main

import (
	"bytes"
	"fmt"
	"github.com/garyburd/redigo/redis"
	. "github.com/kisielk/og-rek"
	"time"
)

func main() {
	type RQJob struct {
		created_at string
		result     string
		ended_at   string
		data       string
		status     string
	}

	//encoding stuff
	p := &bytes.Buffer{}
	e := NewEncoder(p)
	f := []interface{}{"add.add", nil, []interface{}{2, 3}, make(map[string]string)}
	e.Encode(f)
	fmt.Println("encoded value", string(p.Bytes()))

	job := make(map[string]string)
	job_id := "23"

	//pushing encoded value in redis
	c, err := redis.Dial("tcp", ":6379")
	if err != nil {
		panic(err)
	}
	defer c.Close()

	job["data"] = string(p.Bytes())
	queue_id := "rq:job:" + job_id

	_, err = c.Do("HMSET", redis.Args{queue_id}.AddFlat(job)...)
	if err != nil {
		fmt.Println("HMSET", err)
	}

	_, err = c.Do("RPUSH", "rq:queue:default", job_id)
	if err != nil {
		fmt.Println("RPUSH", err)
	}

	time.Sleep(2 * time.Second)

	fmt.Println("queue_id", queue_id)
	result, err := redis.String(c.Do("HGET", queue_id, "result"))
	if err != nil {
		fmt.Println("HGETALL", err)
	}
	fmt.Println("values", result)

	/*
			for i := 0; i < len(values); i += 2 {
				//fmt.Println("  %s: %s", redis.Strings(values[i][0], nil), values[i+1])
				key, _ := redis.String(values[i], nil)
				fmt.Println("  %s: %s", key, values[i+1])
			}

			var rqjob RQJob
			if err := redis.ScanStruct(values, &rqjob); err != nil {
				fmt.Println(err)
			}

		fmt.Println("rqjob result", rqjob.result)
	*/

	//decoding encoded value
	buf := bytes.NewBufferString(result)
	dec := NewDecoder(buf)
	v, err := dec.Decode()
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println("decoded value", v)
}
