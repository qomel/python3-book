# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Overview

Educational Python codebase demonstrating Python modules and object-oriented programming concepts. Part of Python 3 learning exercises.

## Running

```powershell
python main.py
```

## Architecture

- `main.py` - Entry point with exercise functions (`nine_10`, `nine_11`)
- `restaurant.py` - `Restaurant` class demonstrating basic OOP (attributes, methods)
- `user.py` - Class hierarchy: `User` → `Admin`, plus composition with `Privileges` class

The code demonstrates:
- Module imports
- Class inheritance (`Admin` extends `User`)
- Composition (`Admin` has a `Privileges` instance)
