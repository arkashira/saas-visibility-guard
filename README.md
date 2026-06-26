# SaaS Visibility Guard

A Python project that implements a SaaS visibility guard to detect policy violations.

## Features

* Create, edit, and delete policy rules based on SaaS category or domain
* Detect violations automatically
* Send email notifications within 5 minutes of a violation detection
* Get policy violations

## Requirements

* Python 3.8 or later

## Installation

1. Clone the repository
2. Install the dependencies using `poetry install`
3. Run the tests using `pytest`

## Usage

1. Create a policy rule using `create_policy_rule`
2. Detect violations using `detect_violations`
3. Get policy violations using `get_policy_violations`
