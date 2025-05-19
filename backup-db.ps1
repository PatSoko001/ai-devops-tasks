$DB_NAME = "app_database"
$BACKUP_DIR = "C:\Backups\DB"
$DATE = Get-Date -Format "yyyyMMdd_HHmmss"
$FILENAME = "$BACKUP_DIR\$DB_NAME" + "_$DATE.sql.gz"


if (-Not (Test-Path -Path $BACKUP_DIR)) {
    New-Item -ItemType Directory -Path $BACKUP_DIR | Out-Null
    Write-Host "Utworzono katalog $BACKUP_DIR"
}


Write-Host "Rozpoczynam backup bazy $DB_NAME..."


cmd /c "mysqldump -u root -p $DB_NAME | gzip > `"$FILENAME`""

if ($LASTEXITCODE -eq 0) {
    Write-Host "Backup zakończony sukcesem: $FILENAME"
} else {
    Write-Host "Błąd podczas wykonywania backupu!"
    exit 1
}
