# Log Analyzer CLI

A lightweight Python command-line tool for analyzing log files.

## Features

- Counts total log entries
- Counts INFO, WARNING, and ERROR messages
- Groups repeated error messages
- Extracts and counts IP addresses
- Filters logs by log level
- Accepts a log file through CLI arguments
- Handles missing files gracefully

## Requirements

- Python 3

## Usage

Analyze a log file:

```bash
python3 log_analyzer.py sample.log
```

Filter by log level:

```bash
python3 log_analyzer.py sample.log --level ERROR
```

### Available levels

```text
INFO
WARNING
ERROR
```

### Show help

```bash
python3 log_analyzer.py --help
```

## Example Output

```text
Log Analysis Report
-------------------
Total lines: 9
INFO: 4
WARNING: 2
ERROR: 3

Error details
-------------
Database connection failed: 2
Connection timeout: 1

IP statistics
-------------
Unique IP addresses: 3
192.168.1.10: 4
192.168.1.20: 2
192.168.1.30: 2
```

## Example Log Format

```text
2026-09-12 10:02:05 INFO User connected IP=192.168.1.10
2026-09-12 10:04:33 ERROR Database connection failed IP=192.168.1.10
2026-09-12 10:07:45 WARNING High CPU usage IP=192.168.1.20
```

## Project Status

Version 1.0.0 is released and ready to use.

Current functionality includes log-level statistics, error analysis, IP statistics, CLI filtering, and file error handling.
