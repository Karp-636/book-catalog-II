# Book Catalog II

Your library catalog is taking off!  Patrons want to actually *borrow* books, so you need to track which books are checked out and by whom.

In order to gain this new functionality, you'll have to modify your [original](https://github.com/CP-Evenings-and-Weekends/book-catalog) `Book` class.

## Requirements

1. Add a method `check_out(borrower)` to your `Book` class that records who currently has the book.
2. Add a method `return_book()` that marks the book as returned (no borrower).
3. Add any necessary instance properties to make 1 and 2 work.  What data structure?  How do you represent "not checked out"?
4. Add a **class variable** that stores every book currently checked out across the entire catalog.
5. Make sure the information stays in sync — when a book is returned, the class-level list should reflect that too.

## Things to think about
- What's the difference between modifying `self.something` vs `Book.something`?
- If two `Book` instances both touch the same class variable, what happens?  Why?
- What should `check_out` do if the book is already checked out?

## Bonus
- Add a `@classmethod` called `currently_checked_out()` that returns the class-level list of checked-out books.
- Add a method `who_has_it()` that returns the current borrower (or `None` if the book is available).

> Stuck? Have a code error? Use the ["4 Before Me"](https://docs.google.com/document/d/1nseOs5oabYBKNHfwJZNAR7GlU0zkZxNagsw63AD7XV0/edit) debugging checklist to help you solve it!
