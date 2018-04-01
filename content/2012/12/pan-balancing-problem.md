Title: Pan Balancing Problem
Date: 2012-12-24
Category: Mathematics
Tags: mathematics, needswork
Authors: Zach McCormick

I haven’t written anything interesting on here in a while, and I’ve recently been sharpening my algorithm
design, algorithm analysis, and general math skills, so here is a short post on one of my favorite kinds of problems!

### Pan Balancing

A pan balance is a balance with two pans suspended from either end of a rod with a pivot in the center. It can
be used as a ternary operator to determine whether or not an object is heavier, lighter, or the same weight as
another object. A fun mathematical brainteaser is determining the minimum number of weighings to find a certain
element in a set, such as the heavy marble in a set of otherwise identical marbles.

### Optimality

Pan balancing can be viewed as a decision tree problem using ternary decision trees. For instance, the classical
pan balance problem is:

You have a pan balance and 8 marbles. They are all identical, except that one is heavier than the other 7. How
can you identify this marble in the fewest number of weighings?

Think about the decision tree for this problem, rather than the algorithm. There are 8 possible results that can
occur: the first marble is the heavy one, the second marble is the heavy one, …, the eighth marble is the heavy
one. This means our decision tree must have at least 8 leaves. We are using a pan balance, which means our decision
tree is ternary, thus we have:

This equation must be solved for d, which is the number of decisions that must be made to get to a result (i.e. the
fewest number of weighings).

Thus, we know that there must exist an optimal algorithm that can always solve this problem using only two
decisions. Can you come up with that algorithm?

### Algorithm

Sometimes deciding the algorithm can be tricky, but a possible way to start is to draw the tree and put each answer
at a leaf, and work your way up. I drew the decision tree with forward knowledge of the answer so that our solution
makes more sense, but this could be done with a full ternary tree of depth 2 and produce a valid result as well.

Our blank decision tree in Figure 1 has 8 leaves, and we fill in the possible end results in Figure 2. To make
this make more sense, let’s add some meaning to the branching order. If the decision branches left, then the
left pan was heavier. If the decision branches right, then the right pan was heavier. If the decision branches to
the middle, then the pans were equal.

Our decision tree in Figure 3 shows the next level filled in with statements. Intuitively, this makes sense for
results 1, 3, 4, 5, 6, and 8, but why does 1=3 imply 2 and 6=8 imply 7? This is the next step, as we could have
switched 2 and 7’s positions in this tree and our deduction so far is still correct.  What do we know about the
first decision from this? We know that based on the first decision, if the weighing branches to the left, the result
must be 1, 2, or 3. Similarly, if it branches to the right, it must be 6, 7, or 8. If the two pans are equal, then
the answer must be 4 or 5. What comparison can we do to first to guarantee all of these cases for the second level?

Figure 4 shows the correct decision for the first level, and thus completes our decision tree. Try picking any of the
marbles to be the heavier marble and walking through the tree. You will always get the correct result in two weighings!

### Adding Complexity

Now let’s imagine we have 8 coins, and at most one of them is bad, meaning it is either lighter or heavier than
the other ones. How many weighings does it take to determine if one of the coins is bad? How many weighings does
it take to determine which coin it is, and if it is heavier or lighter?

The first question should be simple. There are two possibilities, either one of the coins is bad, or they are all
good! Putting 4 on one side and 4 on the other will answer this question! If they are equal, then there is no bad
coin, but if they are not, then there must be a bad coin!

The second question is harder. What if we use our decision tree from the last problem. We weigh {1,2,3} against {4,5,6}
and it branches left. We then weigh 1 against 3 and it branches to the middle. Does this mean 2 is our bad coin?

Not necessarily! What if 7 was lighter than the rest? Then {1,2,3} would branch left against {6,7,8} and 1 would
branch to the middle against 3. This gives us an answer of 2 but that is clearly not the case!

How many different results are there in this case? Well, 1 could be lighter. 1 could also be heavier! The same
for 2 through 8. Also, they could all be the same! This gives us 8 results for a light coin, 8 for a heavy coin,
and 1 for the same! That is 17 possible results. Our 2-level decision tree can’t determine the answer for a
question with 17 distinct possibilities! A 3-level ternary decision tree can though (why is this?)!

Figure 5 shows a much less intuitive filled-in decision tree for this problem. 1 means 1 is heavier, and 8’
means 8 is lighter, while “x” means there is no bad coin. Since it has only 3 levels, we know it is an optimal
algorithm. Can you derive a different optimal algorithm for this? How many coins at most could we test using only
3 decisions? (i.e. could we do this with 9 coins? 10 coins? More?)

Bonus questions: How many decisions does an optimal algorithm take to identify at most 2 bad coins out of 36
and their relative weights? How many decisions does an optimal algorithm take to identify 3 bad coins out of 36
ignoring their weights? Are there situations where it takes n decisions to identify a single bad coin out of m
coins ignoring their weights, as well as n decisions to identify a single bad coin out of m coins and determining
its relative weight? (i.e. it takes just as many steps to determine the weight too as it does to ignore it)
