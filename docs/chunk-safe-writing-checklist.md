# Chunk-Safe Writing Checklist

A checklist for writing or reviewing knowledge base content that will be split into chunks and searched by an AI. It isn't specific to FinFlow and works for any knowledge base.

## The four rules

### 1. Keep conditions with their outcomes
**Rule:** every sentence with "if" has its "then" (or its consequence) in the same section.
**Why:** a condition without its outcome is useless to a reader, or a search system, that only sees that one chunk.
**Check:** look for "if," "when" and "in the event that." Confirm the outcome is in the same section, not the next paragraph or the next chunk over.

### 2. Keep steps together, and say how many there are
**Rule:** a numbered process states its total step count upfront ("There are 4 steps..."), and all the steps sit together in one section.
**Why:** if chunking still separates a step from the list, the stated count signals that something is missing, instead of the list silently stopping short.
**Check:** for any numbered list, confirm the count comes before the list and the whole list is in one section.

### 3. Every section stands on its own
**Rule:** each section makes sense without the sections before or after it. Words like "this," "that" or "the above" are fine inside a section, but never point across a section boundary.
**Why:** the chunker doesn't know your sections are related. If "this" refers to something in another section, chunking can separate them.
**Check:** for any word pointing backwards, confirm what it refers to is in the same section.

### 4. Every section answers one real question
**Rule:** before writing a section, you must be able to state the specific question it answers. If you can't name a real question that this section, and only this section, fully answers, merge it into one that does or cut it.
**Why:** a section can be well written and self-contained and still be useless as a search result if it doesn't settle an actual question.
**Check:** write down the question each section answers before finalizing it. In this knowledge base, that question is the section's heading.

## How to use it

- **Writing new content:** apply all four rules at the outline stage, before writing any prose. Decide the section boundaries and confirm each one answers a real question.
- **Reviewing existing content:** use the four rules as a pass or fail test on each section.

## Two related habits

- **Links need to stand alone too.** A pointer to another article includes that article's title plus a one-line summary of what it covers, so a reader who only sees that chunk isn't stuck. This is rule 3 applied to links.
- **Repeat the minimum, point for the rest.** Repeat the short facts a section needs to make sense on its own (for example, what "restricted" means). Point to another article for anything with steps or detail.

## What it doesn't catch

It catches problems with structure. It doesn't catch:
- **Wording gaps:** the customer's words differ from the article's.
- **Coverage gaps:** the answer doesn't exist anywhere in the knowledge base.

Those need different tools.
