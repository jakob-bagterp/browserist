---
title: How to Boost Performance in Web Scraping
description: Learn how to speed up your web scraping and browser automation with Browserist by disabling images or running browsers in headless mode and in parallel.
tags:
    - Tutorial
    - Performance
    - Headless
    - Disable Images
---

# How to Boost Performance 🏎️
Running multiple browsers in parallel can take a lot of time and resources. If you apply the right strategy, you can more the workflow much more efficient. Find tips and tricks to speed up your web scraping and browser automation.

## Headless Mode
A browser use many resources to render graphics on the screen. By running it in [headless mode](headless.md), no window is opened and the browser runs in the background. This is an easy way to boost performance and reduce resource usage.

## Disable Images
The largest payload for a web page is often image files. If you don't need images for your workflow and want to improve performance, you can [disable images](disable-images.md) for the browser.

## Parallelization
If you need to run multiple browser instances in parallel, you can try various [parallelization methods](parallelization/results-summary.md):

* [Asynchronous](parallelization/2-asynchronous.md)
* [Multi-threading](parallelization/3-multi-threading.md)
* [Multi-processing](parallelization/4-multi-processing.md)

These methods can also be combined with [headless mode](headless.md) and [disabling images](disable-images.md) for even more efficiency.

## Support the Project
If you have already downloaded and tried the package, perhaps you would like to support its development?

!!! tip "Become a Sponsor"
    If you find this project helpful, please consider supporting its development. Your donations will help keep it alive and growing. Every contribution, no matter the size, makes a difference.

    [Donate on GitHub Sponsors](https://github.com/sponsors/jakob-bagterp){ .md-button .md-button--primary }

    Thank you for your support! 🙌
