# Finding Problems

Project for managing findings security issues found during scans.

* Manage findings
* On command retrieves all the findings for the target with id.
* Filter by definition_id and scan

## Installing / Getting started
* git clone https://github.com/AlenOl/finding-problems

####
* To retrieves all the findings for the target with id use command:
python manage.py closepoll <target_id>
* Use the command line to filter the findings by definition id and scan. Example:
http://127.0.0.1:8000/api/finding/?definition_id=0fR9GA5lgbo6&scans=21JdPvc55BK6