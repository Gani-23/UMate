# UMATE

UMATE (Unified Automation and Testing Engine) is a customized API designed to facilitate rapid automation using API requests. This API integrates with various automation tools and frameworks, providing a streamlined interface for executing automated tasks.

## Overview

UMATE simplifies the automation process by exposing a set of endpoints that accept JSON payloads to define and execute automation tasks. This README provides an introduction to the API, usage examples, setup instructions, contribution guidelines, and licensing information.

## Usage

### Sample JSON Payload for POST Method

The following example demonstrates how to structure a JSON payload to execute automation tasks via UMATE:

```json
{
  "tests": [
    {
      "title": "Open google.com",
      "steps": [
        "Open Browser  https://google.com",
        "Go To  https://google.com"
      ]
    }
  ]
}
