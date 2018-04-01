apr 1, 2013
# Quant Interview Questions (part 3)

I should be studying for a math test right now, but my brain needs a break from groups, subgroups, factor groups, rings, and fields (for my test on Wednesday) and from almost linear systems of differential equations and matrix exponentiation (for my test tomorrow morning), so here are the details of another one of my interviews!

This one was definitely more computer science-y than the rest.

### Question

**Implement a heap data structure with the following methods that run in the following amounts of time, prove their runtime, and meet the extra specifications:**

1. **Create heap in constant time**

1. **Add a new element in log(n) time**

1. **Retrieve the minimum element in constant time**

1. **Remove the minimum element in log(n) time**

1. **Data structure must be entirely immutable**

1. **Data structure must be a balanced binary heap**

### Answer

I started out with no immediate idea how to do this in an immutable way, so I just went ahead and started out with a static create() method (I did this in Java) that returned a HeapNode<T> object. It was obviously constant time.

I knew that I needed to make a min-heap, so I went ahead and started on the add() method. I either set the left-child pointer to a new HeapNode containing the Object to be added if it didn’t have a left child, or I called add() recursively on the left child. Likewise for the right — for now I chose randomly. I explained to the interviewer that I knew it needed to be balanced, but I’d go back to that after I had the basic methods done first.

Retrieve in constant time was easy — obviously you are just returning the Object held by the top HeapNode.

Removing the minimum element in log(n) time was a bit harder. I remembered my algorithms/discrete structures classes though, and knew you just needed to “bubble down” much like you do with add(), so I wrote the code to move the furthest-down node to the top, then keep swapping it with lower elements until the heap property was fulfilled. Again, I knew that it needed to be immutable and balanced, but I wanted a working heap first.

Now that I had the 3 main methods of my heap finished, I worked on the balanced part. I decided that each node should keep track of the number of its left and right children. This works perfectly instead of my random approach from before for add(), so I went ahead and changed this. As for remove(), I had to go back and change this to bubble down to keep it balanced (remove the top node and replace it with the top node of the left or right subtree — whichever has more elements, then swap recursively to maintain heap structure).

Now, about 45 minutes into the interview, I had the correct methods commented with very terse proofs of runtime, but without the immutability property. After pondering aloud for a couple of minutes about it, the interviewer gave me some sort of advice (I don’t remember exactly since the interview was over a month ago), and, due to lack of time, I explained how I would implement the immutability:

### “The Cool Part**”

** denotes my personal opinion!

Think about a min heap with elements (from top to bottom and left to right) 12, 7, 9. To insert 8, you will create a heap that looks like 12, 8, 9, 7 (where 12 is on the 0th row, 8 and 9 are on the 1st row, and 7 on the 2nd row). You might immediately think, “Oh, I need to swap the left-child pointer on 12 to 8, then point 8’s left-child pointer to 7.” This is correct for a mutable heap, but I need to preserve the original heap.

To preserve both heaps, instead create a new HeapNode with 12 as the element. Next, decide if you are going to add to the left or right subtree (you know the sizes). If you are going to add to the left, then set the right-child pointer of the new HeapNode to the original HeapNode containing 9. Next, at 7, you decide if 8 will replace 7 or descend — it is greater, so it replaces 7, so go ahead and create a new HeapNode with 8 inside, and point your new HeapNode with 12’s left-child pointer to this new HeapNode with 8 inside. Finally, create a new HeapNode with 7 inside, and point this new HeapNode with 8’s left-child pointer to this node. Return the new HeapNode with 12 as the element, and you now have a pointer to the old, still-the-same heap, and the new, changed heap too.

Notice that we have changed NONE of the pointers in the original heap, thus we have achieved immutability. We only created 3 new nodes (since for the right subtree, we just pointed the new root to the old right subtree), which is still log(n) time for our heap.

You can continue this process of creating new branches in log(n) time, and while you may generate an ugly looking diagram of pointers if you draw it out, you achieve immutability even with the runtime requirements.

I’ll leave the remove() method in an immutable way as an exercise to the reader!

### Sad News

I couldn’t quite meet all of these requirements in the 50 minutes or so I was allotted, so I unfortunately did not get the job. I admit fully that I came to this interview less prepared than the other ones (the other 3 interviews, I had studied at least 30 hours the week prior to each one; and for the whole set of interviews, I had probably studied probability, combinatorics, data structures, and algorithms for about 200 hours from November through February).

I am still very interested in computational finance, and may apply to some of these firms again in the future post-PhD, as I think it would be thrilling to work on “the street” with some of the greatest mathematicians alive, but for now, I’ll focus more on my research!
