[CmdletBinding()]
param(
  [string]$Url = "http://localhost:5173" # placeholder dashboard URL
)

$ErrorActionPreference = "Stop"
Write-Host "Opening dashboard in default browser: $Url"
Start-Process $Url