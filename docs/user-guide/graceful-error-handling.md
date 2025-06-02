---
title: Measure Time without Blocking Code
description: How Timer for Python gracefully handles exceptions and non-blocking code to ensure that your application keeps running without interruption.
tags:
    - Features
---

# Graceful Error Handling and Non-Blocking Code

!!! success "No Interruptions"
    Timer for Python won't break your code!

This is our commitment.

We aim to avoid randomly raised errors or exceptions. Timer for Python is designed with several nested `try`/`catch` clauses, so it can handle exceptions gracefully and therefore shouldn't cause your application to break while it is running.

Unlike traditional timers, which can halt execution, Timer for Python is non-blocking. This allows your code to run uninterrupted and do what it needs to do.
