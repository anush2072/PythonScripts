
aws-cli command to move files from one s3 bucket to another
```
nohup aws s3 mv s3://source-bucket/source-folder/ s3://destination-bucket/destination-folder/ --profile your-profile --recursive > move_log.txt 2>&1 &
```

-- monitoring
tail -f move_log.txt


Apart from tail -f move_log.txt (which shows real-time output), here are ways to monitor if the S3 move is completed:
1. Check Process Status
Find the process ID (PID) of the nohup command: `ps aux | grep "aws s3 mv"`
If no process is listed, the command has finished.
