Title: DevOps and Horizontal Scaling: Part 2
Date: 2017-06-29
Category: Engineering Management
Tags: software development, engineering management, teams, tools
Authors: Zach McCormick

Lets talk about the first 3 of the 7 tools I described in the last post!

## Product Management involving feature flags, switches, and samples

Product management has a simple sort of flow to it — tickets and feature requests come in, things are prioritized
between managers of different teams, and the end result gets put into a pipeline for engineers to work on. Ideally
the flow is smooth and reliable, with refactoring and testing getting their fair share of time as well. In practice,
most organizations are way behind where they’d like to be, so these things get de-prioritized.

In my opinion, based on my time either working at or working for a number of companies that develop software, the
first box to check in product management is just having a workflow that can be tracked — do you know the mean
time between a bug being reported and it being fixed? What about a simple feature request? Obviously the variables
involved make it so that these numbers don’t fit into a nice and tidy box like “how many widgets did our old
factory produce, and how many does our new one produce?”, but they’re still important to keep track of. I deem
this “level one” of product management.

“Level two” of product management is not much harder — just make sure the rest of the organization is aware
of bug fixes and finished features. Some organizations use JIRA, which can be set up in a way to notify requestors
about the status of their request, or post updates to Slack when releases get pushed to production. Automating
this process is “level two”. You’d be surprised just how happy people get when they have some semblance of
an idea of what’s going on in the engineering department related to their needs!

“Level three” of product management, however, involves adding a significant QA process to the mix. Putting
aside the “developer-centric” parts of QA (code reviews, testing, CI), this should involve at least some
process at the roll-out level. Maybe you have a QA person or QA team that evaluates features in your development
and staging deployments — this is a great first step — but changing the culture to liberally use feature flags,
feature switches, and sampled roll-outs will bring you to “level three”. If you roll something out that has
a deleterious effect, you ought to be able to quickly roll it back out. With feature flags and switches, this is
easy to do without redeploying or merging hot-fixes into your production environment. If you aren’t sure about a
particular feature — especially revamps of UI/UX — you’ll learn to love sampling your releases — releasing
only to select sets of users at once.

These capabilities give you real-time control over your product allowing your engineering team to continue with
their normal flow instead of needing to respond to emergencies on a regular basis. This allows you to keep adding
engineers to your team while remaining efficient.

## Consistent, Realistic Development (and Staging) Environments

Consistent environments in your development and staging environment (hosted) and for your engineers locally is
key to continued success as more people work on more and more complex features.

“Level one” here is simply having a procedure for engineers to run a production-like environment on their own
machine. Without this, deployments are dangerous and feature release can be troublesome. The technologies don’t
need to mirror each other — for instance you might actually be deploying load-balanced Docker containers to
a Kubernetes cluster, but locally you can run manage.py runserver and achieve 99% the same result — but they
should be similar enough that you rarely run into issues in production that you don’t have locally.

“Level two” is where architecture and the “ops” part of DevOps comes into play — ideally your system
should operate as stateless-ly as possible. If you have your database running separate from your application server,
your ElasticSearch cluster in its own world, and your cache running in its own universe, then you’re well on
your way to achieving “level two”. That kind of separation allows you to test your services independently and
substitute out equivalent (but less complex/costly) services locally or on development/staging environments.

The last, and often neglected, level of Realistic Environments is having similar (but sanitized) data available
in different environments and locally. It’s tough to work on pagination algorithms, document search features,
or speeding up high-throughput views with a cache without having sufficient or realistic data to test locally. This
is something else that lends itself well to automation on the “ops” side of DevOps. A daily/weekly/etc. Jenkins
job that takes a database or cache backup, sanitizes out sensitive information, and stores it in S3 can save you
from countless production deployments solving problems that only exist on production.

With these strategies in place, “tribal knowledge” of how systems work starts to go away and onboarding new
engineers becomes a piece of cake, allowing you to scale your team more effectively.

## Extensive Automated Testing and Continuous Integration

The last of the three tools I’m going to talk about in this post is testing. It may seem obvious, given the
number of “How to Test using JUnit” talks at local meetups, but testing should be your best friend. Countless
bad deployments are saved due to effective unit and integration tests every day.

The first hurdle is simply test coverage, and reporting on test coverage. A simple and effective KPI (though remember,
engineering can be fuzzy and full of variables, so you can’t worship the KPI) is test coverage. Several derivatives
exist, such as “test coverage of critical paths”, but having a few of these reported on weekly can be a great
tool to keep the team abreast of how well-tested your code is. This might involve unit tests, integration tests,
load tests, or more, but the first step is simply having the tests available and running/reporting on them on occasion.

The second hurdle is automating those tests — this could be as simple as a Jenkins job that runs ./manage.py
test on every PR and before deploying to development/staging environments. It may involve a suite of tests,
or involve more complex testing frameworks like Cucumber using Behavior-driven Development. Knowing when tests
fail and responding to them quickly and effectively is “level two” in this realm. I’m a big fan of using
Cucumber or Behave — two Python frameworks for BDD — because of the ability to create cross-products of tests
easily. This might be something like end-to-end tests of eCommerce, where each product has a suite of 50 tests
run on it, and simply adding 3–4 additional product codes actually runs an additional 150–200 tests.

The final stage of effective automated testing is actually less about testing and more about culture/product
management. It takes more time to implement, being a culture thing, but part of the bug reporting/fixing process
should involve unit and integration tests to prevent regressions from occurring more than once. Users are frustrated
when things break, but they’re even more frustrate when the same thing breaks a second time. This one is a little
more loose, as there isn’t a framework you can add or a tool you can use to solve it instantly, but is a great
goal to try to achieve when it comes to automated testing.

With this kind of testing in place, engineers don’t need to know every last detail and caveat of system
functionality — they can just start coding features and fixing bugs in their first couple of weeks.

## How do you do it?

Careful planning and working with the engineering team and outside product owners/users is critical to implementing
these steps successfully. This is actually something that I love to consult with companies about — shoot me an
e-mail at [zach@trailblazingtech.com](mailto:zach@trailblazingtech.com) to get a bit more information about that. I
love traveling and will gladly come to you wherever you are to help your company succeed in implementing these tools.

## What next?

In my next post, I’ll go over the last 4 tools to implementing a DevOps culture to enable Horizontal Scaling
within an engineering organization. Stay tuned!
