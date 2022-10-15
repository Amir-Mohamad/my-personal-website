### The polymorphism design 

at the first we use comment and reply system using this way, but later we found that it could be bad
for rest of features such as like and dislike.

## Q: Why we cant use polymorphism in like and dislike system ?

in this case we should return a response that uses the article/parent data
and if we use ploymorphism we cant access to the detailed data in each instance
(becuase of differnt names in each response: article/book/parent).

## what features can use polymorphism system
seems using ploymorphism system can be used in comment/reply crud and other features that they dont
need to access the detailed data in instances (ex: like/dislike)


## Why we remove lists ?
lists are not too much usefull in the v1
we grow the category feature instead



