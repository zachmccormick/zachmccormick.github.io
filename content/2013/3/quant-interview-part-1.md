Title: Quant Interview Questions (part 1)
Date: 2013-3-14
Category: Mathematics
Tags: mathematics, software development
Authors: Zach McCormick

I finally have a free moment (I should be doing work, but I don’t have any crazy deadlines to meet today),
so I thought I would start posting the questions and answers to one of my recent job interviews, as I found them
incredibly interesting and thought provoking. In fact, I would say that their interview process rekindled a love
of mathematics that I once had, and lost in high school due to the sheer amount of busywork I was made to do in
the “accelerated track” at my school.

### Background

I interviewed for a developer position at one of the top quantitative/proprietary trading firms out there, and thus
they are looking for the cream of the crop in terms of quantitative reasoning and programming ability. I had four
interviews over the phone, of which the first three went well, but I struggled a bit with the fourth. I applied
to a handful of other similar firms and have not heard back from any of them.

### Difficulty of quant programming positions

For reference, they all required practically every math-related statistic about me they could before the interviews:
my GPA is about 3.55 out of 4 at a top 20 school, I scored an 800 on the math part of the SAT, an 800 on the
Math II SAT Subject Test, a 36 on the math part of the ACT, and a 168 out of 170 on the quantitative part of the
GRE. All of this was required to submit an application to most firms. I applied to about 20 of these firms and
was only approached by 1, so you have been warned! :-)

### Question

The first question was “**given an input stream, how would you collect a k-sized evenly-distributed sample of
the input?**”’

### Constraints and clarification

First, to answer these types of questions, you need to fully understand the question and all of the constraints. First,
I asked about data types — are these numbers? are they objects? — and the interviewer told me it didn’t matter,
but we could pretend they are integers for now and move to the general case later. Next, I asked about total size
— my intuition first says that I need to know the size of the sample space in order to sample it. He said “input
stream” is meant to be like an iterator — you just keep calling next() until it stops returning results —
so you don’t know the total size of the set. I next asked “okay, so if we start at 0, we always know how many
we have *at each step*, right?” to which he answered, “yes.” At this point, I could restate the problem in a
more explicit form: “Given an input stream of objects, how would you collect a k-sized evenly-distributed sample
of the input, *so that at any point in time, you have a k-sized evenly distributed sample of the input **so far.***”

### How to start

Next, I started typing out the code (we used a Google Docs-esque screen sharing thing to share coe). I knew that,
given a constant K, I would always need to iterate through the first k items and add them to the sample. Based on
the intuitive concept: If you have k items, then a k-sized sample includes all of the items.

### Inductive step

Next, the hard step: how do I determine whether or not the k+1'th item goes into the sample set or does not? If
it does, which item does it replace?

It turns out, as long as we keep a running count of how many items we’ve seen so far, let’s say y, then we
just need to roll a y-sided die to determine whether or not it goes in the sample. If you roll a 1, 2, …, or a
k, then it goes in the sample. If you roll a k, k+1, …, y, it does not. If it goes in the sample, then you roll
a k-sided die to determine the index of the element it replaces. This can then be proven to work inductively and
thus answers the theoretical question. Programmatically, I implemented this with the Random class of Java.

### Concrete Example

Consider a 6-sized sample of natural numbers. We fill it at first with 1, 2, 3, 4, 5, and 6. Next we get a 7. We
roll a 7-sided die (or in the program, we generate a random number from 1 to 7). We get a 5. Since 1 <= 5 <= 6,
we put 7 in the sample. We roll a 6-sided die (generate a random number from 1 to 6). We get 4. So now we replace
4 in the set, so our sample looks like {1, 2, 3, 7, 5, 6}.

1, 2, 3, 4, 5, and 6 all had a 100% chance to be in the sample. With the 7th item, they all need to have a 6/7
chance of being in the sample for it to be evenly distributed. The roll for 7 makes sense, since it had a 6/7
chance of being in the sample just based on its roll. Anything currently in the sample, in our case 4, now has a
1/6 chance of not being in the sample. Thus, we get a (6/7)*(1/6)=1/7 chance of not being in the sample REGARDLESS
of the result of the roll for 7, thus giving it a 6/7 chance of being in the sample, just like 7 has based on its roll.

Cool math, eh?
