# AWS Infrastructure Health Monitor

## Overview

AWS Infrastructure Health Monitor is a Python-based monitoring tool that collects and evaluates health metrics for EC2 instances using AWS CloudWatch. It supports CPU, memory, and disk utilization checks, handles stopped instances and missing metrics gracefully, and produces clear per-instance health summaries.

This project demonstrates real-world DevOps and SRE practices including AWS API integration, observability, edge-case handling, and automation-ready design.

**************
## Technologies Used
* Python 3
* AWS EC2
* AWS CloudWatch
* Boto3
* YAML configuration
* AWS CloudWatch Agent (for memory & disk metrics)

**************

## 📂 Project Structure

```text
aws-infra-health-monitor/
├── monitor.py          # Main execution script
├── config.yaml         # AWS configuration and thresholds
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```
**************

## ⚙️ Prerequisites
* Python 3.9+
* AWS account with EC2 instances
* IAM permissions:
* ec2:DescribeInstances
* cloudwatch:GetMetricData
* AWS CLI configured or environment variables set
* CloudWatch Agent installed on EC2 instances (for memory & disk metrics)

**************

## 🔧 Configuration (config.yaml)

thresholds:
  cpu: 80
  memory: 80
  disk: 80

**************

## ▶️ How It Works

* Discovers all EC2 instances and their states.
* Builds CloudWatch metric queries for:
* CPU utilization (native EC2 metrics)
* Memory and disk usage (CloudWatch Agent metrics)
* Fetches metrics for the last 15 minutes in UTC.
* Handles edge cases:
* Stopped instances
* Missing CloudWatch Agent metrics
* Compares metric values against defined thresholds.
* Prints a consolidated health report per instance.

**************

## 📊 Sample Output
Instance: i-0931f85b4bc81ca44 | Name: prod-web-01
  - AWS/EC2 CPUUtilization: OK (22.34%)
  - CWAgent mem_used_percent: NO DATA
  - CWAgent disk_used_percent: ALERT (91.12%)
--------------------------------------------------

**************

## 🚨 Alert Logic
Condition	Status
Metric missing	NO DATA
Metric below threshold	OK
Metric above threshold	ALERT
Instance stopped	SKIPPED

**************

## 🧠 Design Highlights

* Uses immutable Instance IDs for metric correlation
* Enriches output with EC2 Name tags
* Batch CloudWatch metric queries for efficiency
* Timezone-aware UTC timestamps
* Configuration-driven thresholds
* Production-ready error handling

**************

## 🚀 Future Enhancements

* SNS / Email notifications
* JSON output for integrations
* AWS Lambda deployment
* Auto-detection of CloudWatch Agent
* Support for Auto Scaling Groups