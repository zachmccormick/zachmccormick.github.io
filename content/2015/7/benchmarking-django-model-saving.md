Jul 7, 2015
# Benchmarking Django Model Saving

When using Django’s ORM as a basis for data harvesting (probably not the best idea in the first place, but sometimes it’s easier to go with what you know), I learned that Django isn’t exactly crazy fast when saving models to the database. Here are some stats on doing different things with Django to try to speed it up.

First, I wrote two methods and used cProfile to profile them. MyModel is a model with a single max_length=100 CharField.

    def benchmark():
     for i in range(1, 10000):
     x = MyModel(data=”Some Random Data”)
     x.save()

    def benchmark_bulk():
     items = []
     for i in range(1, 10000):
     x = MyModel(data=”Some Random Data”)
     items.append(x)
     MyModel.objects.bulk_create(items)

I used cProfile to profile these methods, using SQLite as the backing database. benchmark() took 14.87 seconds, and benchmark_bulk() took 0.400 seconds. Obvious improvement there by using bulk_create, but you can’t use FKs to link subrecords to the records, as the pk property of those objects will not get set.

When switching to MySQL: 8.09 seconds on benchmark() and 0.379 seconds on benchmark_bulk(). A little bit better — definitely better on benchmark, but not that much better when bulk inserting.

When switching to Postgres: 6.71 seconds on benchmark() and 0.385 seconds on benchmark_bulk(). Even faster on benchmark, but not any faster for bulk insertion. Bulk insertion may be effectively capped out on speed. The bulk_create method on query.py seems to take about .2 seconds no matter the backend.

Switching to Cassandra led to bulk_create not working, and benchmark() took 17.88 seconds! That wasn’t what I expected here! Looking at the profiler stats, it seems it spent 11.63 seconds in time.sleep(), so maybe I’m doing something wrong — subtracting these two gives 6.25 seconds, which is closer to what I’d expect.

Obviously the use cases here are very simple, but for simple model insertion speed, Postgres seems to win if you want a relational database and migrating to new software isn’t hard. If you don’t want to use Postgres (in our case, we like MySQL), or you need intense speedups, then modify your code to use bulk_create()!

I’ll make another post later this week or next week, with a more complicated, real-world data structure, and show how (likely) Cassandra would beat out both MySQL and Postgres for saving more complex models quickly, since we can eliminate FK relationships and save objects in a more NoSQL fashion. This comes at a querying and filtering cost, so I’ll examine those too!
