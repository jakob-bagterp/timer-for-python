---
title: Measure Time without Blocking Code
description: How Timer for Python gracefully handles exceptions and non-blocking code to ensure that your application keeps running without interruption.
tags:
    - Features
---

# Graceful Error Handling and Non-Blocking Code

!!! success "No Interruptions"
    Timer for Python won't break your code!

Timer for Python is designed with several nested `try`/`catch` clauses so it gracefully handles exceptions and therefore shouldn't break your application while running.
