import subprocess

# comando PowerShell que será executado
ps_script = r"""
regsvr32 hnetcfg.dll

$m = New-Object -ComObject HNetCfg.HNetShare

$m.EnumEveryConnection |% { $m.NetConnectionProps.Invoke($_) }

$c = $m.EnumEveryConnection |? { $m.NetConnectionProps.Invoke($_).Name -eq "Ethernet" }

$config = $m.INetSharingConfigurationForINetConnection.Invoke($c)

Write-Output $config.SharingEnabled

Write-Output $config.SharingType

$config.DisableSharing()

$config.EnableSharing(0)
"""

# chama o PowerShell para executar o comando
result = subprocess.run(["powershell", "-Command", ps_script], capture_output=True, text=True)

# imprime a saída do PowerShell
print(result.stdout)
