# AWS nohup Command Instruction Manual

## Overview

`nohup` (No Hang Up) is a Unix command that allows you to run processes that continue running even after you log out of the terminal or close the session. When combined with AWS CLI commands, it's particularly useful for long-running operations like deleting large S3 folders, copying data between buckets, or running extended data processing tasks.

## What nohup Does

1. **Prevents Hang Up**: Keeps the command running even if the terminal session ends
2. **Output Redirection**: Automatically redirects output to a file named `nohup.out` (unless specified otherwise)
3. **Background Execution**: Runs the command in the background, freeing up your terminal

## Basic Syntax

```bash
nohup [command] [arguments] > [output_file] 2>&1 &
```

### Components Explained

- `nohup`: The command that prevents the process from being terminated when the session ends
- `[command]`: The actual command you want to run (e.g., `aws s3 rm`)
- `[arguments]`: Any parameters for your command
- `> [output_file]`: Redirects standard output to a file
- `2>&1`: Redirects standard error to the same place as standard output
- `&`: Runs the command in the background

## AWS CLI Examples

### 1. Deleting Large S3 Folders

```bash
# Delete a single folder
nohup aws s3 rm s3://your-bucket/large-folder/ --recursive --profile your-profile > delete_log.txt 2>&1 &

# Delete multiple folders (run individually)
nohup aws s3 rm s3://your-bucket/folder1/ --recursive --profile your-profile > delete_folder1.log 2>&1 &
nohup aws s3 rm s3://your-bucket/folder2/ --recursive --profile your-profile > delete_folder2.log 2>&1 &
```

### 2. Copying Large Amounts of Data

```bash
# Copy between S3 buckets
nohup aws s3 cp s3://source-bucket/ s3://destination-bucket/ --recursive --profile your-profile > copy_log.txt 2>&1 &

# Sync directories
nohup aws s3 sync /local/path/ s3://your-bucket/remote-path/ --profile your-profile > sync_log.txt 2>&1 &
```

### 3. Running Long AWS Operations

```bash
# Start a long-running Glue job
nohup aws glue start-job-run --job-name my-long-job --profile your-profile > glue_job.log 2>&1 &

# Batch processing with Step Functions
nohup aws stepfunctions start-execution --state-machine-arn arn:aws:states:region:account-id:state-machine:my-machine --profile your-profile > sf_execution.log 2>&1 &
```

## Managing nohup Processes

### Check Running Processes

```bash
# List all background jobs
jobs -l

# Find nohup processes
ps aux | grep nohup

# Check process status
pgrep -f "aws s3"
```

### Stop a nohup Process

```bash
# Using kill with PID
kill [PID]

# Using killall (be careful!)
killall nohup

# Using job control
kill %1  # Where %1 is the job number from jobs -l
```

### View Output

```bash
# View the log file
tail -f delete_log.txt

# Check the last 100 lines
tail -n 100 delete_log.txt

# Follow multiple logs
tail -f *.log
```

## Best Practices

### 1. Always Use Specific Log Files

```bash
# Good: Specific log file
nohup aws s3 rm s3://bucket/folder/ --recursive > delete_folder_$(date +%Y%m%d_%H%M%S).log 2>&1 &

# Avoid: Default nohup.out
nohup aws s3 rm s3://bucket/folder/ --recursive &
```

### 2. Include Timestamps in Logs

```bash
# Add timestamp to log entries
nohup bash -c 'aws s3 rm s3://bucket/folder/ --recursive | while read line; do echo "$(date): $line"; done' > delete_log.txt 2>&1 &
```

### 3. Use AWS Profiles for Multi-Account Access

```bash
# Explicit profile
nohup aws s3 cp s3://source/ s3://dest/ --recursive --profile production > prod_copy.log 2>&1 &

# Multiple accounts
nohup aws s3 sync s3://dev-bucket/ s3://prod-bucket/ --profile dev > dev_to_prod.log 2>&1 &
```

### 4. Monitor Progress

```bash
# Create a monitoring script
nohup bash -c '
while true; do
    echo "$(date): Checking progress..."
    aws s3 ls s3://your-bucket/folder/ --recursive --summarize | tail -5
    sleep 300  # Check every 5 minutes
done
' > monitor_progress.log 2>&1 &
```

## Troubleshooting

### Common Issues

1. **Permission Denied**: Ensure AWS credentials are properly configured
   ```bash
   aws configure --profile your-profile
   ```

2. **Process Stops Unexpectedly**: Check logs for errors
   ```bash
   cat nohup.out
   # or your specific log file
   cat delete_log.txt
   ```

3. **Terminal Hangs**: Use proper background execution
   ```bash
   # Ensure you have the & at the end
   nohup command > log.txt 2>&1 &
   ```

### Recovery After Logout

If you've logged out and need to check on your nohup processes:

```bash
# SSH back into the server
# Check if processes are still running
ps aux | grep nohup

# Check log files
ls -la *.log
tail -f delete_log.txt
```

## Advanced Usage

### 1. Parallel Operations

```bash
# Run multiple deletions in parallel
for folder in folder1 folder2 folder3; do
    nohup aws s3 rm s3://bucket/$folder/ --recursive --profile your-profile > delete_$folder.log 2>&1 &
done
```

### 2. Error Handling

```bash
# Retry failed operations
nohup bash -c '
for i in {1..3}; do
    aws s3 cp s3://source/ s3://dest/ --recursive && break
    echo "Attempt $i failed, retrying..."
    sleep 60
done
' > retry_copy.log 2>&1 &
```

### 3. Resource Monitoring

```bash
# Monitor CPU and memory usage
nohup bash -c '
aws s3 cp s3://large-bucket/ s3://dest/ --recursive &
PID=$!
while kill -0 $PID 2>/dev/null; do
    echo "$(date): Process $PID still running"
    ps -p $PID -o pid,ppid,cmd,%mem,%cpu
    sleep 60
done
echo "$(date): Process completed"
' > monitor.log 2>&1 &
```

## Quick Reference Cheat Sheet

```bash
# Basic nohup AWS command template
nohup aws [service] [operation] [parameters] --profile [profile-name] > [log-file].log 2>&1 &

# Check running jobs
jobs -l

# Kill a process
kill [PID]

# View logs
tail -f [log-file].log

# Common AWS services with nohup
nohup aws s3 cp/rm/sync/mv [s3-path] --recursive > s3_operation.log 2>&1 &
nohup aws ec2 start-instances --instance-ids i-1234567890abcdef0 > ec2_start.log 2>&1 &
nohup aws rds create-db-instance --db-instance-identifier mydb > rds_create.log 2>&1 &
```

## Safety Considerations

1. **Test First**: Always test commands without nohup first
2. **Double-Check Paths**: Verify S3 paths before deletion
3. **Monitor Resources**: Don't overload your system with too many parallel operations
4. **Keep Logs**: Save logs for audit and troubleshooting
5. **Use Dry Runs**: For destructive operations, use `--dryrun` flag first

## Conclusion

`nohup` is an essential tool for running long-lasting AWS CLI operations without worrying about session timeouts. By following the practices outlined in this manual, you can reliably execute AWS operations that run for hours or even days, with proper logging and monitoring capabilities.


## Example

```bash
# Delete multiple folders from an S3 bucket
nohup aws s3 rm s3://your-bucket-name/folder-jan2025/ --recursive --profile your-profile > delete_jan2025.log 2>&1 &

nohup aws s3 rm s3://your-bucket-name/folder-feb2025/ --recursive --profile your-profile > delete_feb2025.log 2>&1 &

nohup aws s3 rm s3://your-bucket-name/folder-mar2025/ --recursive --profile your-profile > delete_mar2025.log 2>&1 &

nohup aws s3 rm s3://your-bucket-name/folder-apr2025/ --recursive --profile your-profile > delete_apr2025.log 2>&1 &

nohup aws s3 rm s3://your-bucket-name/folder-may2025/ --recursive --profile your-profile > delete_may2025.log 2>&1 &

nohup aws s3 rm s3://your-bucket-name/folder-jun2025/ --recursive --profile your-profile > delete_jun2025.log 2>&1 &

nohup aws s3 rm s3://your-bucket-name/folder-july2025/ --recursive --profile your-profile > delete_july2025.log 2>&1 &
```