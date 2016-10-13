# mongodb101

[M101P: MongoDB for Developers][1] course code by MongoDB University

## Table of Content

 - [Chapter 1: Introduction](notes/WEEK1.md)
 - Chapter 2: CRUD
 - Chapter 3: Schema Design
 - Chapter 4: Performance
 - Chapter 5: Aggregation Framework
 - Chapter 6: Application Engineering
 - Chapter 7: Case Studies
 - Final Exam

## MongoDB Docker Container

```bash
docker run --name mongodb \
    -v /home/pavel/dev/git_reps/mongodb101/week1/db:/data/db \
    -d -P mongo
```

 [1]: https://university.mongodb.com/courses/M101P/about
