Title: DevOps and Horizontal Scaling: Part 1
Date: 2017-06-28
Category: Engineering Management
Tags: software development, engineering management, teams, tools
Authors: Zach McCormick

How do engineering departments scale beyond teams of 10–15 people and stay nimble?

Let’s imagine scaling an engineering department that starts with 3 employees and an “efficiency factor”
of 100%(bear with me). You hire a couple more experienced engineers, start having daily stand-ups and a weekly
planning meeting and compared to your previous “efficiency rating”, you’re now outputting the work of 5
engineers at 90% efficiency — not bad!

The business starts to need more things, and managing tickets and support requests start to become a task of their
own, so your efficiency drops to around 75%. You hire a product manager and a support engineer, bringing you up
to 7 employees and back to an efficiency rating around 95%(your core engineers are no longer managing tickets or
support requests).

Time continues and business is good, but as the features keep piling on — internal CRM features, ERP features for
driving workflow, eCommerce features for increasing sales — things start to break down. Deployments aren’t as
smooth or fast as they used to be, minor feature additions are breaking existing features, and bug fixes are slow
due to the manual testing involved.

You’re smart and have faced these types of multifaceted problems before, so you focus on an easy win:
infrastructure. You hire an infrastructure engineer to sort out deployments and scaling. While she’s getting
integrated with the team, you start a feature freeze to work on better testing. Things seem to be looking up —
engineering KPIs are stabilizing and people *feel* good about it.

Time moves on, you have occasional cycles of writing lots of tests, and you start to accept the occasional
deployment hiccup as a fact of life. You aren’t too concerned with that engineering efficiency rating anymore
(which is hovering around 50%) because the product has just gotten larger and that’s how software works —
isn’t the phrase “oh look at that big and slow-moving company” just normal?

**It does not have to be!**

This is where complacency stops engineering teams from achieving the very possible horizontal scaling that many
hugely successful companies achieve. With the right investment in **DevOps**, horizontal scaling is absolutely
possible beyond 10, 20, 50, or even 100 engineers.

**DevOps** is a phrase that gets used a lot for a lot of different reasons, so let’s start with a couple definitions:

**DevOps**— a portmanteau of “development” and “operations”. A combination of the engineers who write new
features and the IT staff that keep the servers running. DevOps is an umbrella term for a culture of collaboration
between these participants in the organizational software lifecycle.

**Horizontal Scaling** — the ability to scale by adding more resources to your pool of resources. Note that
this isn’t vertical scaling — adding more powerful resources (i.e. a superstar engineer), but simply adding
more resources.

I like to think of implementing “the DevOps culture” as something like an organization adopting Six Sigma
or Kaizen — it’s a set of tools with a cohesive purpose that you can pick and choose from to address your
needs. What are those tools, then?

1. Product Management involving feature flags, switches, and samples

1. Consistent, Realistic Development (and Staging) Environments

1. Extensive Automated Testing and Continuous Integration

1. Manual **and** Automated Code Review

1. Scalability through PaaS & Non-monolithic Architecture

1. Logging, Instrumentation, and Monitoring

1. Architecture Review Team

In my next post, I’ll go over each of these tools, tying them back to the ultimate goal of keeping “engineering
efficiency” high while allowing an organization to scale horizontally in engineering team size.
