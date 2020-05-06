## Prompt

We have supplied you with a `master_list`, which is a collection of book recommendations from famous authors. Assume that this list could grow arbitrarily large in size.

Your task is to write a program that returns *all* books that have been recommended `n` times. Decide which data is important to return.

You may write the program in whatever programming language you feel most comfortable, however we would prefer you choose the language relevant to the role you are interviewing for (likely javascript or golang).

Please ask us questions, use Google, or consult documentation if you get stuck. There are many possible solutions here, so we are more interested in the process.

You may practice this exercise in advance if you so choose, but you will be asked to implement from scratch as part of the assessment.

## Things to Note:
- There may be multiple books recommended `n` times. They all must be returned.
- There may be duplicate book titles, but every Title:Author combination is unique.
- Some entries do not have data for every field.

## Desired Behavior:
```bash
$ ./book-parser 5
# [ <all books that have been recommended exactly 5 times> ]
```

## Time

30 minutes
