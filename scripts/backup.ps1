[CmdletBinding()]
param(
  [switch]$DryRun = $true,
  [string]$Provider = $env:CLOUD_BACKUP_PROVIDER,   # "aws"|"azure"|"gcp"
  [string]$BucketOrContainer = $env:CLOUD_BACKUP_BUCKET, # naam bucket/container
  [string]$Prefix = "wonderwoman/backup"
)

$ErrorActionPreference = "Stop"
Write-Host "=== Wonderwoman Backup ==="
Write-Host "Provider: $Provider"
Write-Host "Target: $BucketOrContainer"
Write-Host "DryRun: $DryRun"

if (-not $Provider -or -not $BucketOrContainer) {
  Write-Host "[SKIP] Secrets CLOUD_BACKUP_PROVIDER en/of CLOUD_BACKUP_BUCKET ontbreken."
  exit 0
}

# Verzamel artefacten
$timestamp = (Get-Date).ToString("yyyyMMdd-HHmmss")
$archive = "backup-$timestamp.zip"
Write-Host "Archiveren naar $archive ..."
Compress-Archive -Path "wonderwoman","docs" -DestinationPath $archive -Force

if ($DryRun) {
  Write-Host "[DRYRUN] Upload zou plaatsvinden naar $Provider:$BucketOrContainer/$Prefix/$archive"
  exit 0
}

switch ($Provider.ToLower()) {
  "aws"   { aws s3 cp $archive "s3://$BucketOrContainer/$Prefix/$archive" --only-show-errors }
  "azure" { az storage blob upload --container-name $BucketOrContainer --file $archive --name "$Prefix/$archive" --only-show-errors }
  "gcp"   { gsutil cp $archive "gs://$BucketOrContainer/$Prefix/$archive" }
  default { throw "Unsupported provider: $Provider (use aws|azure|gcp)" }
}

Write-Host "Backup klaar: $archive"