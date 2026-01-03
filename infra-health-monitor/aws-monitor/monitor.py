#---------------- EC2 Instance Monitorning -------------------

import boto3
import yaml
from datetime import datetime, timedelta, timezone


# -----------------------------
# Load configuration
# -----------------------------
with open("config.yaml") as f:
    config = yaml.safe_load(f)

cpu_threshold = config["thresholds"]["cpu"]
mem_threshold = config["thresholds"]["memory"]
disk_threshold = config["thresholds"]["disk"]

REGION = "us-east-1" # you can change if required

# -----------------------------
# AWS Clients
# -----------------------------
ec2_client = boto3.client("ec2", region_name=REGION)
cloud_watch_client = boto3.client("cloudwatch", region_name=REGION)


# -----------------------------
# Discover EC2 instances + state
# -----------------------------
instance_reservations = ec2_client.describe_instances()
instances_details =  []
for each_reservation in instance_reservations["Reservations"]:
    for each_instnace in each_reservation["Instances"]:
        instances_details.append({
            "id": each_instnace["InstanceId"],
            "state": each_instnace["State"]["Name"]
         }
        )

# -----------------------------
# Time window for CloudWatch
# -----------------------------
end_time = datetime.now(timezone.utc)
start_time = end_time - timedelta(minutes=15)


# -----------------------------
# Metrics to query
# -----------------------------
metrics_config = [
    {'name': 'CPUUtilization', 'namespace': 'AWS/EC2'},
    {'name': 'mem_used_percent', 'namespace': 'CWAgent'},
    {'name': 'disk_used_percent', 'namespace': 'CWAgent'}
]

print("\n----- AWS EC2 Health Check -----\n")

# -----------------------------
# Build & send queries PER INSTANCE
# -----------------------------


for instance in instances_details:
    instance_id = instance["id"]
    state = instance["state"]
    #EDGE CASE 1: Instance stopped
    if state != "running":
        print(f"{instance_id} | STATE: {state.upper()} | CPU: N/A | SKIPPED")
        continue

    queries_list = []

    for metric in metrics_config:
        metric_name = metric["name"]
        metric_namespace = metric["namespace"]
        safe_id = f"m_{instance_id.replace('-', '_')}_{metric_name.lower()}"
        
        # Build the config for THIS specific metric/instance
        config = {
            'Id': safe_id,
            'MetricStat': {
                'Metric': {
                    'Namespace': metric_namespace,
                    'MetricName': metric_name,
                    'Dimensions': [{'Name': 'InstanceId', 'Value': instance_id}]
                },
                'Period': 300,
                'Stat': 'Average'
            }
        }
        queries_list.append(config)


# 2. Send the whole queries list to AWS at once to get all metrics values
response = cloud_watch_client.get_metric_data(
    MetricDataQueries=queries_list,
    StartTime=start_time,
    EndTime=end_time
)

# creating alerts by using metrics data response
instance_alerts = {}
for result in response["MetricDataResults"]:

    metric_id = result["Id"]
    values = result["Values"]
    label = result["Label"]

    instance_id = "_".join(metric_id.split("_")[1:3])

    if instance_id not in instance_alerts:
        instance_alerts[instance_id] = []

    if not values:
        instance_alerts[instance_id].append(f"{label}: NO DATA")
        continue

    value = values[-1]

    if "CPUUtilization" in label:
        threshold = cpu_threshold
    elif "mem_used_percent" in label:
        threshold = mem_threshold
    elif "disk_used_percent" in label:
        threshold = disk_threshold
    else:
        continue

    if value > threshold:
        instance_alerts[instance_id].append(f"{label}: ALERT ({value:.2f}%)")
    else:
        instance_alerts[instance_id].append(f"{label}: OK ({value:.2f}%)")


# -----------------------------
# Print final status per instance
# -----------------------------
for instance_id, alerts in instance_alerts.items():
    print(f"\nInstance: {instance_id}")
    for alert in alerts:
        print(f"  - {alert}")
    print("-" * 50)
