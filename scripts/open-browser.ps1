[CmdletBinding()]
param(
  [string]$Url = "http://localhost:8080",
  [switch]$Edge,
  [switch]$Chrome,
  [switch]$Firefox
)

$ErrorActionPreference = "Stop"

function Try-Open($exe, $args) {
  if (Get-Command $exe -ErrorAction SilentlyContinue) {
    Start-Process $exe $args
    return $true
  }
  return $false
}

Write-Host "Opening browser to $Url ..."

if ($Edge)    { if (Try-Open "msedge"  $Url) { return } }
if ($Chrome)  { if (Try-Open "chrome"  $Url) { return } }
if ($Firefox) { if (Try-Open "firefox" $Url) { return } }

# Probeer in volgorde: Edge, Chrome, Firefox, anders default handler
if (Try-Open "msedge"  $Url) { return }
if (Try-Open "chrome"  $Url) { return }
if (Try-Open "firefox" $Url) { return }

Start-Process $Url
