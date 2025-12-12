# PowerShell script to replace all occurrences of 'yeison' or 'Yeison' with 'michael' in contents and rename files/directories containing 'yeison'.
# Usage: Run in project root: .\scripts\replace_yeison_with_michael.ps1

param (
    [string]$Root = "C:\Users\SENA\Downloads\3-TRI-MALAVER-main\3-TRI-MALAVER-main",
    [switch]$DoRenameFiles = $true,
    [switch]$DoReplaceContents = $true,
    [switch]$DryRun = $false
)

# File extensions to operate on for content replacement
$exts = @('*.js','*.py','*.html','*.htm','*.md','*.txt','*.json','*.csv','*.sql','*.jsx','*.ts','*.tsx','*.css','*.scss','*.java','*.c','*.cpp','*.h','*.hpp')

Write-Output "Root: $Root"
Write-Output "DryRun: $DryRun"

function Replace-ContentInFile {
    param($path)
    try {
        $content = Get-Content -Raw -LiteralPath $path -ErrorAction Stop
        $newContent = [regex]::Replace($content, 'yeison', 'michael', 'IgnoreCase')
        if ($newContent -ne $content) {
            if ($DryRun) {
                Write-Output "[DRY] Would replace in: $path"
            }
            else {
                Set-Content -LiteralPath $path -Value $newContent -Encoding UTF8
                Write-Output "Updated content: $path"
            }
        }
    } catch {
        Write-Warning "Failed to read/replace ${path}: $($_.Exception.Message)"
    }
}

function Rename-Path {
    param($oldPath)
    $dir = Split-Path $oldPath -Parent
    $name = Split-Path $oldPath -Leaf
    $newName = $name -replace '(?i)yeison','michael'
    if ($newName -ne $name) {
        $newPath = Join-Path $dir $newName
        if ($DryRun) {
            Write-Output "[DRY] Would rename: $oldPath -> $newPath"
        }
        else {
            if (-not (Test-Path $newPath)) {
                Rename-Item -LiteralPath $oldPath -NewName $newName
                Write-Output "Renamed: $oldPath -> $newPath"
            }
            else {
                Write-Warning "Target exists, skipping rename: $newPath"
            }
        }
    }
}

# Create backup folder
$backup = Join-Path $Root "backup_before_replace_$(Get-Date -Format 'yyyyMMddHHmmss')"
if (-not $DryRun) {
    Write-Output "Creating backup at $backup"
    Copy-Item -LiteralPath $Root -Destination $backup -Recurse -Force -ErrorAction SilentlyContinue
}
else {
    Write-Output "[DRY] Would create backup at $backup"
}

# Replace contents
if ($DoReplaceContents) {
    foreach ($pattern in $exts) {
        Write-Output "Processing files pattern: $pattern"
        $files = Get-ChildItem -LiteralPath $Root -Recurse -File -Include $pattern -ErrorAction SilentlyContinue
        foreach ($file in $files) {
            Replace-ContentInFile -path $file.FullName
        }
    }
}

# Rename files containing yeison
if ($DoRenameFiles) {
    # Rename files first (deepest-first to avoid conflicts), process files that contain 'yeison' in name (case-insensitive)
    $filesToRename = Get-ChildItem -LiteralPath $Root -Recurse -File | Where-Object { $_.Name -match '(?i)yeison' } | Sort-Object FullName -Descending
    foreach ($f in $filesToRename) { Rename-Path -oldPath $f.FullName }

    # Rename directories containing yeison (descend order)
    $dirsToRename = Get-ChildItem -LiteralPath $Root -Recurse -Directory | Where-Object { $_.Name -match '(?i)yeison' } | Sort-Object FullName -Descending
    foreach ($d in $dirsToRename) { Rename-Path -oldPath $d.FullName }
}

Write-Output "Done."
