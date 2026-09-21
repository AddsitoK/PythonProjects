@echo off
:: 1. Comprobar si gsudo esta instalado
where gsudo >nul 2>&1
if %errorLevel% neq 0 (
    echo [ERROR] No se encontro 'gsudo'. Instalalo primero con: winget install gerardog.gsudo
    pause
    exit /b
)

:: 2. Elevar todo el script al nivel divino de TrustedInstaller
gsudo --ti cmd /c "
    echo Deteniendo servicios de Windows Update como TrustedInstaller...
    net stop wuauserv /y
    net stop bits /y
    net stop usosvc /y
    net stop waasmedicsvc /y

    echo Aplicando directivas anti-resurreccion en el Registro...
    reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU\" /v NoAutoUpdate /t REG_DWORD /d 1 /f
    reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU\" /v AUOptions /t REG_DWORD /d 2 /f
    reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\" /v DisableWindowsUpdateAccess /t REG_DWORD /d 1 /f

    echo Deshabilitando los servicios para siempre...
    sc config wuauserv start= disabled
    sc config bits start= disabled
    sc config usosvc start= disabled
    sc config waasmedicsvc start= disabled

    echo ¡Windows Update ha sido destruido por completo! Tu procesador es libre.
"
pause
}