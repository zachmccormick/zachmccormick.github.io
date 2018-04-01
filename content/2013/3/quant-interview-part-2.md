Title: Quant Interview Questions (part 2)
Date: 2013-3-18
Category: Mathematics
Tags: mathematics, software development
Authors: Zach McCormick

Here is another interview question from a separate interview with the same firm:

**“Given the results of a round-robin tournament, can you always create a list of teams ordered such that, when
looking at a single team, the team to its left won against them, and the team to its right was beaten by them?**”

### Clarification

A round-robin tournament, for those who are not familiar with the term, is a tournament where every team plays
every other team once. For example, if you had 16 teams, then each team would play 15 games — one game against
every other team. A concrete example of this question can be stated: 4 teams play a round robin tournament, team
1 beats all of the teams, team 2 beats teams 3 and 4, and team 3 beats team 4. A correct ordering would be [1,2,3,4].

### Proof Strategy

Looking at this problem, my strategy was first to prove it was not impossible with a small number of teams (4
for instance as above), then come up with a strategy from there. It immediately became apparent after giving one
concrete case that I could do this quickly and succinctly through a proof by induction.

### Induction

Base Case The base cases could be n=0. A tournament of 0 teams has a sequence of no elements and is properly
ordered. Next, we can try n=1, which has a sequence of one element and is properly ordered. Next, we can look at n=2
and we start to see what our inductive step is going to look like. With n=2, either team 1 beat team 2, or team 2
beat team 1, giving us two orderings: [1,2] or [2,1] respectively.  Inductive Hypothesis The inductive hypothesis
is that we have a tournament of n teams with a properly ordered sequence. Essentially, as in any inductive proof,
we assume that this situation exists (we have shown it for n=0, 1, and 2, so it must exist for at least 3 values
of n).  Inductive Step The inductive step is to look at the situation of n+1 teams. Consider our original n teams,
with a correctly ordered sequence such as [1, 2, 3, …, n-1, n]. When we add team n+1, let us first prepend it
to the front of the sequence, so we have [n+1, 1, 2, 3, …, n-1, n].

If team n+1 beat team 1, then we have a satisfactory ordering, because the subsequence [1, 2, 3, …, n-1, n]
must still be correct, and the introduced relationship of team n+1 beating team 1 is correct.

If team n+1 lost to team 1, then try moving it one position to the right, to get [1, n+1, 2, 3, …, n-1, n]. If team
n+1 beat team 2, then we have a satisfactory ordering, because it lost to team 1, beat team 2, and the subsequence
[2, 3, …, n-1, n] must still be correct.

If team n+2 lost to team 2, then continue moving it to the right. Continue this process until a correct sequence
is found, or until you reach the end of the list. If team n+1 reaches the end of the list, then it must have lost
to team n, thus the subsequence [1, 2, 3, …, n-1, n] must be correct and the introduced relationship of team
n+1 losing to team n is correct, thus the ordering must be correct.

Conclusion Thus, we have proven that it is ALWAYS possible to order a round-robin tournament as such. Generating such
an ordering using this method would take O(n²) time. On further consideration of generating this ordering given this
data, it became apparent that one could adapt merge-sort to reduce this sequence generation to O(n log n) time. Due
to this being a comparison sort, this is absolutely the best we can do (maybe I’ll prove this another time!).
