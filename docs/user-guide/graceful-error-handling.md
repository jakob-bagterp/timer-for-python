---
title: Measure Time without Blocking Code
description: How Timer for Python gracefully handles exceptions and non-blocking code to ensure that your application keeps running without interruption.
tags:
    - Features
---

# Graceful Error Handling
Timer for Python is designed with several nested `try`/`catch` clauses so it handles exceptions gracefully and therefore shouldn't break your application while running.
