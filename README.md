# sgrstore

**sgrstore** is a simple program command line utility written in Python (3.6) that can interact with a sqlite database.

## Overview

I wrote this program as a personal project for organizing storage bins in my home. Right now, this program can do three things:

* Add item records
* Check in / out items from storage
* Search for items
* List all items with columns as filters

This program is a thin wrapper for executing basic SQL commands. My goals are to use this to help organize my home. It is also my first step to learning more about database design and how to interact with a database.

## How to use

This program is specifically designed for a database I've already made; it can't create a database on its own. If you're interested in copying this, you can modify it to meet your own database needs.

That said, I used sqlite to make this, so your mileage may vary.