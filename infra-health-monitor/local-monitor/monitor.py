import psutil
import yaml
import subprocess
import logging
import sys

# -----------------------------
# Logging configuration
# -----------------------------
logging.basicConfig(
    filename="health_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------
# Load configuration
# -----------------------------
with open("config.yaml") as f:
    config = yaml.safe_load(f)

cpu_threshold = config["thresholds"]["cpu"]
mem_threshold = config["thresholds"]["memory"]
disk_threshold = config["thresholds"]["disk"]
services = config["services"]

# -----------------------------
# Collect system metrics
# -----------------------------
cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage("C:\\").percent

print("\n----- System Health Report -----")
print(f"CPU Usage    : {cpu}%")
print(f"Memory Usage : {memory}%")
print(f"Disk Usage   : {disk}%")

logging.info(f"CPU Usage: {cpu}%")
logging.info(f"Memory Usage: {memory}%")
logging.info(f"Disk Usage: {disk}%")

# -----------------------------
# Threshold validation
# -----------------------------
issues_found = False

if cpu > cpu_threshold:
    print("⚠️ CPU usage exceeds threshold")
    logging.warning("CPU usage exceeds threshold")
    issues_found = True

if memory > mem_threshold:
    print("⚠️ Memory usage exceeds threshold")
    logging.warning("Memory usage exceeds threshold")
    issues_found = True

if disk > disk_threshold:
    print("⚠️ Disk usage exceeds threshold")
    logging.warning("Disk usage exceeds threshold")
    issues_found = True

# -----------------------------
# Service status check (Windows)
# -----------------------------
def check_service(service):
    try:
        subprocess.check_output(
            ["powershell", "-Command", f"Get-Service -Name {service}"],
            stderr=subprocess.DEVNULL
        )
        return "RUNNING"
    except subprocess.CalledProcessError:
        return "NOT RUNNING"

print("\n----- Service Status -----")
for svc in services:
    status = check_service(svc)
    print(f"{svc}: {status}")
    logging.info(f"Service {svc}: {status}")

    if status != "RUNNING":
        issues_found = True

# -----------------------------
# Final health decision
# -----------------------------
print("\n----- Overall Status -----")
if not issues_found:
    print("✅ System is HEALTHY")
    logging.info("System health check passed")
    sys.exit(0)
else:
    print("❌ System needs ATTENTION")
    logging.error("System health check failed")
    sys.exit(1)
