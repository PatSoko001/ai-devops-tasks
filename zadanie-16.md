Zadanie 16: Przekonwertowanie skryptu bash na PowerShell

Cel
Celem było przepisanie skryptu Bash do tworzenia backupu bazy danych w systemie Linux na jego odpowiednik PowerShell, działający pod Windows.


 Kluczowe różnice między Bash a PowerShell
Aspekt	Bash	PowerShell
Zmienne	$VAR="wartość"	$VAR = "wartość"
Interpolacja	"${VAR}" i "$VAR"	"$VAR"
Tworzenie katalogu	mkdir -p "$DIR"	New-Item -ItemType Directory -Path $DIR
Sprawdzanie katalogu	[ ! -d "$DIR" ]	if (-Not (Test-Path $DIR))
Operacje na dacie	$(date +%Y%m%d_%H%M%S)	Get-Date -Format "yyyyMMdd_HHmmss"
Obsługa błędów	if [ $? -eq 0 ]; then ...	if ($LASTEXITCODE -eq 0) { ... }
Uruchamianie narzędzi systemowych	mysqldump	gzip


Uwagi praktyczne
PowerShell nie ma natywnych narzędzi mysqldump i gzip. Konieczne jest użycie:

WSL (Windows Subsystem for Linux),

zewnętrznych wersji mysqldump.exe i gzip.exe,

lub pełnej platformy Docker/Linux.

Ścieżki w Windows wymagają backslashy (\), ale PowerShell potrafi też obsługiwać slashy (/) przy użyciu zmiennych środowiskowych.


Podsumowanie
Skrypt Bash został skutecznie przepisany na PowerShell z zachowaniem funkcjonalności. Największe różnice dotyczą składni, obsługi daty, ścieżek i środowiska powłoki. PowerShell oferuje większe możliwości integracji z systemem Windows, ale wymaga dostosowania w przypadku narzędzi typowo uniksowych.
