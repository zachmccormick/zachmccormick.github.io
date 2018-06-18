Title: Code Vision
Date: 2018-06-18
Category: Software Development
Tags: software architecture, engineering management, teamwork, refactoring, change
Authors: Zach McCormick

While I'm currently on an early flight from Indianapolis to Newark, I'd love to expound on
some thoughts I've had recently about what I call "code vision". I define this as a written,
iterated-on plan for what a codebase should look like in the future. This is different from
what features are in the pipeline - think more of a big-picture, directional plan for the
architecture. I believe that this holistic view is needed as a codebase accumulates age and
a significant number of active developers, much like a past-startup-stage company needs
vision and values. *I believe the process of refactoring to be largely ineffective without
first having this vision*.

As a former Boy Scout, I have heard the phrase "Try and leave this world a little better
than you found it" by Robert Baden-Powell more times than I can count, and I try to remember
it in many different contexts - code included. I think that this is easier to apply with
nature and the outdoors - "better" is quite clear to us: reduce waste, don't pollute, and
try not to disturb the wildlife. Software is a bit different, however, in that "better" is
often a very subjective thing. Refactoring - the process of leaving the codebase a little
better than you found it - can be quite aimless unless we have a common concept of "better".

Imagine that you have a class that is ugly - it has one gigantic method. You break
it up into a series of smaller functions that are easier to test, and call them procedurally
from one "master" method or function. Your comments make it clearer what is going on, but
ultimately the class performs the same function. If you have several classes with similar
structure - one big method or several small, well-commented methods - all wired together
without a class hierarchy or unifying framework, you've only put lipstick on a pig. Your
system itself is still disorganized, so you find some commonalities between parts - say
you are rendering HTML pages and you create a base `Controller` class to take care of
authorization, or you are processing SQL-driven reports, so you create a `SqlReport`
base class and rewrite several classes to use this new class hierarchy. Without a holistic
vision, it's likely that the next person to work on rendering pages or generating reports
will do their own thing or simply pattern match (i.e. copy, paste, and modify) without
thinking about how their additions or changes fit into the greater picture. This leads to
JSON API controllers using a base `Controller` class geared toward rendering HTML and
large bits of transactional SQL statements using a `SqlReport` class geared toward
asynchronous queries run on a read replica.

I have worked at a number of companies, but most of them had relatively young codebases,
with fewer than 20 or 30 developers and fewer than 5 years of history. I've had, however,
the benefit of working on contracts or patent cases where I've been privy to much, much
larger and older codebases as well, and have seen ones with clear and obvious vision, as
well as ones without. Needless to say, the ones without were the least organized, the
least understandable, and the hardest to understand. The ones with vision tended to share
several common, positive values: *clarity, modularization, and simplicity*. Moreover,
they tended to exhibit what I refer to as "**framework-oriented thinking**" - an
architectural approach that favors frameworks written by architects and senior
engineers with components and extensions built by everyone. These are inherently
modular, and often were surprisingly simple and clear. One only had to read the docs
for the major framework components - often base classes or abstract classes that
made up a pipeline, a composite rendering framework, or a communication paradigm -
in order to understand the big picture. From there, any individual components made
sense. It is easy to understand the purpose and function of `FanOutPipelineTask` or
`class ColoredButton extends Button (extends UIComponent)`, and one couldn't (without
significant effort, anyway) try to shim a subclass of `SqlReport` to run on the
write primary!

New development aside, with this level of increased clarity and understanding, the process
of refactoring changes from a cloudy, somewhat aimless task to one that has purpose and is
rather easy to understand. With a code vision and "framework-oriented thinking", one can
evaluate methods, classes, and components and ask themselves "does this component fit into
the paradigm of the framework as is?" and if the answer is no, then ask "should this
component change, or should the framework change?". Methods can still be divided into
less complex sub-methods, but now classes and components can be changed with purpose - to
better fit into the rest of the system. Code review changes as well - a reviewer can now
ask "do these additions or changes fit in with the framework, or change the framework
itself to better suit its purpose?" rather than simply "does this code function properly
and is it tested appropriately?".

I'd love to hear your thoughts on this concept. Shoot me an email at
[z@z11k.com](mailto:z@z11k.com) or find me on LinkedIn - I'm a sucker for organization
and structure, but I love hearing the other side as well - maybe you have a good reason
that such vision and structure hinders feature progress or is overly prescriptive. Let
me know and let's discuss to make the software world a better place!
