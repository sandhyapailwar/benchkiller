# Project description
## STATEMENT OF GOALS

Main goal of the project is to create a system that sends personalized e-mails to appropriate key persons based on preselected data and provides control of correspondence flow.
The end user of the system is defined as TFS or/and ST lead.


## FUNCTIONAL DESCRIPTION

The system must have User Friendly Interface for:
•	Uploading Global Demand Excel table;
•	Filtering data;
•	Adding and selecting letter template;
•	Attaching CV presentations;
•	Sending letters; 
•	Providing letter correspondence status.

Database of the system should be built considering functional scalability and integration with other systems

Future functionality includes but is not limited to integration with Accenture Maximize system, automatic Selection of CVs to be attached based on project role requirement, classification of replies.


## BUSINESS PROCESS DESCRIPTION

1) Filters are applied to Global Demand table (GD.xlsx) to preselect project with D&A roles and EU region.
2) Rows containing key contacts that already received a letter are removed (info from CRM table).
3) Rows are split between spam bot team (SBT) members.
4) SBT sends letters with a help of basic scripts that are using a letter template, personalizing that template by addressing key person by name, adding project and role info from GD.xlsx and attach one pptx presentation of all currently available employees and interns.
5) Replies from key persons are handled manually. 
6) Each evening SBT meats to fill in CRM table to control correspondence flow: add key contacts to whom letter was sent, change correspondence status of all rows based on received replies, discuss escalation necessity of specific correspondence to ST leads

# License
<table>
  <thead>
    <tr>
      <th>Package Name</th>
      <th>License Name</th>
      <th>Link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Python 3.5.6</td>
      <td>PSF LICENSE AGREEMENT FOR PYTHON 3.5.6</td>
      <td>https://docs.python.org/3.5/license.html</td>
    </tr>
  </tbody>
</table>

# Readme revision log
<table>
  <thead>
    <tr>
      <th>Date</th>
      <th>User</th>
      <th>Change log</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>31.10.2018</td>
      <td>nikolajs.selpackis</td>
      <td>Readme.md created</td>
    </tr>
    <tr>
      <td>20.03.2018</td>
      <td>marina.olina</td>
      <td>Readme.md modified</td>
    </tr>
  </tbody>
</table>

## Deployment

----

### Python dependencies

```bash
sudo apt install -y \
    build-essential \
    libssl1.0.2 \
    libssl-dev \
    libsqlite3-dev \
    openssl \
    libbz2 \
    libbz2-dev \
    python3-dev \
    python3-pip \
    python3-virtualenv
```

### Create virtualenv

```bash
# By default should work:
virtualenv $(which python3) .venv
# or another way to do the same:
python3 -m virtualenv .venv
```

### Activate virtualenv

```bash
source .venv/bin/activate
```

### Install necessary dependencies

```bash
pip install -r requirements.txt
```

### Enable check before commitment to Repository

```bash
pre-commit install
```

### Manual python code style check

```bash
pre-commit run
```


### Start Python web server

```
./manage.py runserver
```

# Template samples

### Email template sample

```html
<p>Hello {{ contact.full_name }},</p>

{% if role%}

<p>We have candidates for position "{{ role.name }}" at {{ opportunity.opportunity_name }}.

{% else%}

<p>We have some candidates for postitions:</p>

<ul>
{% for op in opportunity_contacts%}
<li>{{ op.role.name }} ({{ op.opportunity.opportunity_name }} (id {{ role.import_key }}))</li>
{% endfor %}
</ul>

{% endif %}

<p>Please see attached CVs and email us in case you are interested in.</p>
```

### To run sending agent

```
in separate terminal!
for dry run:
./agent.py -r <your email>

to send messages to recipients:
./agent.py
```

### Solutions for errors of the agent
```
For Anaconda users:
if you have received recent updates of windows:
1. Uninstall Anaconda
2. Download and install recent version of Anaconda


If you keep getting the error "win32com.gen_py has no attribute 'CLSIDToPackageMap'"
clear contents of C:\Users\<username>\AppData\Local\Temp\gen_py
```
