# Assignment 9

## Task Automation with Cron and At

### Daily File Cleanup
- Deletes all files from `/path/to/home/temp` daily at 2:00 AM.

### Weekly System Backup
- Backs up `/path/to/home/user` to `/path/to/home/user/backups/` every Sunday at 3:00 AM.

### Disk Usage Report
- Sends a daily disk usage report email at 8:30 AM.


## Implementation
1. Open the crontab file
``` bash
    crontab -e
```
2. Copy and paste the cron job commands from the crontab file provided in this directory
3. Save and exit the editor.
4. Verify that the cron jobs have been set up correctly by running:
``` bash
    crontab -l
```
