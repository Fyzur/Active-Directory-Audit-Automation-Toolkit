Import-Module ActiveDirectory

#Group Member Validator
function GroupMemberValidator {
Write-Host "`n`n <--- Welcome To Group Member Validator --->`n`n" -ForegroundColor DarkBlue
$group_name= Read-Host -Prompt "Enter the MiM group Name"
$user_OHID = Read-Host -Prompt "Enter your OHID"
$main_shell = Get-ADGroupMember -Server arnob.local $group_name | Select-String $user_OHID | ForEach-Object {$_.line.split("=")[1].split(",")[0]}

if ($main_shell -eq $user_OHID){
    Write-Host "You are member of $group_name :>`n" -ForegroundColor Green
}
else {
    Write-Host "  No Match Found :<`n" -ForegroundColor Red
}
}

#FindAllMemberinGroup
function FindAllMemberinGroup{
    Write-Host "`n`n <--- Welcome To Member Extractor --->`n`n" -ForegroundColor DarkBlue
$group_name= Read-Host -Prompt "Enter the MiM group Name"
$semiclone= Read-Host -Prompt "With Semiclone ? Y/N"

if ($semiclone -eq ("N" )){
(Get-ADGroup -Server arnob.local -Identity $group_name -Properties *).member |ForEach-Object {$_.split('=')[1].split(',')[0]}
}
elseif ($semiclone -eq ("Y")) {
(Get-ADGroup -Server arnob.local -Identity $group_name -Properties *).member |ForEach-Object {$_.split('=')[1].split(',')[0]} |ForEach-Object { "$_;" }
}
else {
    Write-Host "Something is Wrong!" -ForegroundColor Red
}
}

#GroupExtractor
function GroupExtractor {
   Write-Host "`n`n <--- Welcome To Group Extractor --->`n`n" -ForegroundColor DarkBlue
$user_OHID = Read-Host -prompt "Enter User OHID "
(Get-ADUser -Server arnob.local -Identity $user_OHID -Properties MemberOf).MemberOf |ForEach-Object {$_.split("=")[1].split(',')[0]}
}

#QuickLookUp
function QuickLookUp {
    Write-Host "`n`n <--- Welcome To Quick Lookup --->`n`n" -ForegroundColor DarkBlue
    $user_OHID = Read-Host -prompt "Enter User OHID "

Get-ADUser -Server arnob.local -Identity "$user_OHID" -Properties * 
| Select-Object DisplayName,EmployeeID,EmailAddress,Enabled,Title,Department,Office,Manager,LockedOut,LastBadPasswordAttempt,LastLogonDate,modifyTimeStamp,Created 
|Format-List
}

#Device IP
function DeviceIP {
    $DeviceName = Read-Host -Prompt "Enter your device name"
    Resolve-DnsName -Name $DeviceName
}

#Group Audit
function Group_Audit {
$group_name = Read-Host -Prompt "Enter the MiM group Name"
$csv_path   = Read-Host -Prompt "Enter the output CSV path (e.g. C:\temp\members.csv)"

$group_obj = Get-ADGroup -Server arnob.local -Identity $group_name -Properties Description
$group_des = $group_obj.Description

$user_List = (Get-ADGroup -Server arnob.local -Identity $group_name -Properties member).member | ForEach-Object {
    $adUser = Get-ADUser -Server arnob.local -Identity $_ -Properties EmployeeID, DisplayName -ErrorAction SilentlyContinue
    
    if ($adUser) {
        [PSCustomObject]@{
            EmployeeID       = $adUser.EmployeeID
            FullName         = $adUser.DisplayName
            GroupName        = $group_name
            GroupDescription = $group_des
        }
    }
}

$user_List | Export-Csv -Path $csv_path -NoTypeInformation -Encoding UTF8
Write-Host "`nExtraction complete! Exported to: $csv_path" -ForegroundColor Green
}

#Main Operation Menu
Write-Host "Welcome! Please select one of the options `n" -ForegroundColor DarkMagenta

$menu = @"
-----------------------------------------
 Option | Description
-----------------------------------------
   0    | Group Member Validation
   1    | Find/Extract All Group Members
   2    | Extract All User Groups
   3    | Quick User Lookup
   4    | Group Audit
   9    | Device IP Address Lookup
-----------------------------------------

"@

$user_option = Read-Host $menu "Select one option:"
Start-Sleep -Seconds 15

if ($user_option -eq 0){
    GroupMemberValidator
}
elseif ($user_option -eq 1) {
    FindAllMemberinGroup
}
elseif ($user_option -eq 2) {
    GroupExtractor
}
elseif ($user_option -eq 3) {
    QuickLookUp
}
elseif ($user_option -eq 4) {
    Group_Audit
}
elseif ($user_option -eq 9) {
    DeviceIP
}
else {
    Write-Host"Something is Wrong!"
}

Write-Host "`n`n`n`nThank You "
