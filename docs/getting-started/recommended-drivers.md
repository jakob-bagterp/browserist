---
tags:
    - Automation
    - Chrome
    - Edge
    - Firefox
---

# Recommended Drivers for Browserist
Browserist supports automation with the most popular browser drivers. Find help installing the most common drivers:

* [Chrome](./browsers/chrome.md)
* [Edge](./browsers/edge.md)
* [Firefox](./browsers/firefox.md)

## What is a Browser Driver?
A browser driver is a program that controls a web browser in a similar way to scrolling, clicking and pointing with a mouse on a desktop or gestures on a touchscreen. The driver is responsible for controlling the behaviour of the browser and interacting with the web page by sending commands to the browser and receiving responses.

Since Browserist is based on the [Selenium](https://www.selenium.dev) web driver for browser automation, Selenium is already included in the installation. Now you have to do is install a browser and its corresponding driver:

<table>
    <thead>
        <tr>
            <th>Requirement</th>
            <th colspan="3">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1. Python package</td>
            <td colspan="3"><a href="../installation/">Browserist</a> web automation extension to Selenium</td>
        </tr>
        <tr>
            <td>2. Browser</td>
            <td style="text-align: center;"><a href="../browsers/chrome/">Chrome</a></td>
            <td style="text-align: center;"><a href="../browsers/edge/">Edge</a></td>
            <td style="text-align: center;"><a href="../browsers/firefox/">Firefox</a></td>
        </tr>
        <tr>
            <td>3. Driver</td>
            <td style="text-align: center;">ChromeDriver</td>
            <td style="text-align: center;">Microsoft Edge Driver</td>
            <td style="text-align: center;">GeckoDriver</td>
        </tr>
    </tbody>
</table>

## Why Do I Need a Browser Driver?
While a browser is needed to render the content and graphics of a web page, including communicating with the web page server, it needs a driver to tell it what to do. The driver is responsible for controlling the behaviour of the browser and interacting with the web page.

In other words, the driver replaces your mouse and keyboard with a program that controls the browser.
