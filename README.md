Active Directory Audit Automation Toolkit
A modular PowerShell toolkit designed to streamline IT audit tasks by automating common Active Directory lookups, group validation, and reporting. Built to reduce manual effort, increase audit accuracy, and centralize frequently used AD operations.
Features


Group Member Validation
Quickly verify whether a specific user belongs to a specified AD group.


Group Membership Extraction
Extract all members of an AD group, with optional semicolon-delimited formatting for bulk processing.


User Group Enumeration
Retrieve all AD groups associated with a given user.


Quick User Lookup
Display key AD user attributes, including status, manager hierarchy, and timestamps used in audit analysis.


Device IP Resolution
Resolve device names to IP addresses using DNS, useful for audit or incident response scenarios.


Group Audit Export
Generate and export a full CSV report listing user Employee IDs, names, group name, and description.


Interactive Menu Interface
A simple, menu-driven console to make all functions easily accessible for auditors.


Purpose
This toolkit was created to support IT audit and compliance operations by automating repetitive AD queries, reducing errors, and accelerating validation workflows. It centralizes essential audit utilities into a reusable, scalable script.
Technologies Used

PowerShell
Active Directory Module
DNS Utilities
CSV Data Export

How It Works
Run the script in a PowerShell session with the Active Directory module enabled. The interactive menu lets you select the operation you want to perform. Results display immediately in the console or export to CSV when applicable.

<img width="525" height="254" alt="image" src="https://github.com/user-attachments/assets/96485ca3-5072-4a17-a9b2-8faa5b1ff134" />
