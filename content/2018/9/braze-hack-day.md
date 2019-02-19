Title: Braze Hack Day: Lunch and Learn App
Date: 2018-09-06
Category: Software Development
Tags: product management, software development, projects
Authors: Zach McCormick

For Braze's Hack Day (on which I'm somewhat cheating, because during the actual hack day,
I was in Estonia/Latvia/Lithuania...) I decided to write an application for managing our
Lunch and Learn events - internal talks within Engineering/Product where people can
present something they think is cool that they think other people would also think is
cool! I decided to learn some React and TypeScript, do a full-blown product management
process, follow a rigorous software engineering process, and document the whole thing.
That said, here goes nothing:

## Problem Statement

Going along with the fake Einstein quote below, I decided to spend a bit of time crafting
a well-defined problem statement.

> If I had only one hour to save the world, I would spend fifty-five minutes defining the
> problem, and only five minutes finding the solution. - probably not Albert Einstein

"My coworkers want to submit ideas for Lunch and Learns but there's no clear form or way to
submit such ideas. Moreover, when they tell, Slack, or email me, they have to wait for me
to find a time on the schedule where it will work. Their idea gets lost if I forget to
follow up on the request."

"Moreover, I have found that especially for Lunch and Learn events scheduled too far in
advance, people tend to forget about their presentation and have to cancel last minute. My
two-days-ahead manual reminder system is error-prone and obviously not that effective."

These two statements describe problems for two different audiences: my coworkers and
myself. It doesn't assume a solution but describes the problems both audiences face. It
also provides a few main concepts that can act as a checklist: "way to submit an idea",
"find a time on the schedule", and "reminder system". From these two statements, I think
I can make a product!

## Minimum Viable Product

In a more far-reaching, time-consuming product management lifecycle, I'd probably
advocate for prototyping, customer research, etc., but in this simple case, we can jump
right into a minimum viable product. I'm a bit of a math nerd, so I want to specifically
create a _measurable_ minimum viable product. Each of my three main concepts must have
measures of success to go with them - I may not necessarily create a control and
experiment group (i.e. remind one presenter multiple times, but remind another presenter
only once, two days before the presentation), but I want to be able to look at statistics
and metrics to know whether or not my product is achieving its indended goals.

For "way to submit an idea": I already actually have a timestamped list of the presentation
requests so far thanks to my almost neurotic usage of GTD, so for this, I'll just aim to
keep a daily/weekly/monthly/quarterly count of submitted Lunch and Learns. I can compare
this to my stats from my prior, manual system to see if, by having a submission system,
people are submitting more ideas than before!

For "find a time on the schedule": This is mostly about eliminating the time gap between
submission and scheduling it on the calendar. If I can integrate with our internal Google
Calendar system with available rooms, I can shrink this gap to nearly instantly. This one
probably doesn't have an effective before/after metric.

For "reminder system": I also know (thanks, Gmail and Slack!) who I reminded and when I
reminded them about their presentations. I can quickly figure out the statistics for this,
then calculate the drop-out percentage for the manual system. Moving forward, I can
determine the drop-out percentage for the automatic system and adjust the types and number
of reminders moving forward to achieve an ideal result (not too many reminders, but
enough that few people have to cancel due to being unprepared).

All of this said, here are the user stories for the features of my MVP, in Gherkin-esque
form so that I can use the same definitions in my feature files!:

- As a user, I can sign up/log in via Google SSO so that I can access the app.
  - Scenario: I have a @braze.com email address
    - Given: I click the "Sign in with Google" link on the home page
    - When: I select a @braze.com email address in Google's SSO form
    - Then: I am successfully signed up/logged into my account on the app
  - Scenario: I do not have a @braze.com email address
    - Given: I click the "Sign in with Google" link on the home page
    - When: I select a @gmail.com email address in Google's SSO form
    - Then: I am directed to a page notifying me that the app is for Braze employees only
- As a user, I can view past and upcoming Lunch and Learns.
  - Scenario: What I see when I am logged in and on the home page
    - Given: I am logged in and on the home page
    - Then: There are two tabs on the page: one for "Past Lunch and Learns" and one for
      "Future Lunch and Learns"
    - Then: I can see the future Lunch and Learns in a list
  - Scenario: Viewing future and past Lunch and Learns
    - Given: I am logged in and on the home page
    - When: I click on "Past Lunch and Learns"
    - Then: I can see the past Lunch and Learns in a list
    - When: I click on "Future Lunch and Learns"
    - Then: I can see the future Lunch and Learns in a list
  - Scenario: Viewing a Lunch and Learn's details
    - Given: I am logged in and on the home page
    - When: I click on the title of a Lunch and Learn
    - Then: I am navigated to a details page with more details on that Lunch and Learn

- As a submitter, I want to be able to submit an idea and schedule a Lunch and Learn.
  - Scenario: I am logged in and on the home page
    - Given: I am logged in and on the home page
    - When: I click on the "Submit New Lunch and Learn" button
    - Then: I am navigated to the New Lunch and Learn page
  - Scenario: All form elements must be filled out to submit a Lunch and Learn
    - Given: I am on the New Lunch and Learn page
    - When: I fill out the New Lunch and Learn form
    - When: I do not fill out the Title field
    - When: I press the "Submit" button
    - Then: The Lunch and Learn is not booked
    - Then: I see an error message, requiring the Title field
  - Scenario: Only free slots are shown
    - Given: I am on the New Lunch and Learn page
    - Then: Only free slots on the calendar are shown
  - Scenario: Submit and appropriate slot is still available
    - Given: I am on the New Lunch and Learn page
    - Given: A properly filled out Lunch and Learn form
    - When: The selected timeslot is free
    - When: I press submit
    - Then: The Lunch and Learn is booked
    - Then: A calendar invite is sent to all prospective attendees
  - Scenario: Submit and appropriate slot is no longer available
    - Given: I am on the New Lunch and Learn page
    - Given: A properly filled out Lunch and Learn form
    - When: The selected timeslot is free
    - When: I press submit
    - Then: The Lunch and Learn is not booked
    - Then: I see an error message, requiring a new time slot

- As a scheduled presenter, I want to receive reminders about my Lunch and Learn.
  - Scenario: I want a reminder 2 weeks before my Lunch and Learn
    - Given: I have a lunch and learn scheduled for 2 weeks from now
    - Then: I will receive an email today about my upcoming Lunch and Learn
  - Scenario: I want a reminder 1 week before my Lunch and Learn
    - Given: I have a lunch and learn scheduled for 1 week from now
    - Then: I will receive an email today about my upcoming Lunch and Learn
  - Scenario: I want a reminder 3 days before my Lunch and Learn
    - Given: I have a lunch and learn scheduled for 3 days from now
    - Then: I will receive an email today about my upcoming Lunch and Learn

## Software Engineering

Ok! Time to build something! I decided on using Heroku (as I almost always do)
and my trusty ol' Python/Django starter template for it. I upgraded to 2018
and introduced Webpack, TypeScript, and React, as well as a development
environment hot module reloader. I figured I'd probably be making loads of
mistakes as I learned React, so this seemed important. See the first commit
of my repo to see where I started!


