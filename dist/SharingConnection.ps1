# Register the HNetCfg library (once)
regsvr32 hnetcfg.dll

# Create a NetSharingManager object
$m = New-Object -ComObject HNetCfg.HNetShare

# List connections
$m.EnumEveryConnection |% { $m.NetConnectionProps.Invoke($_) }

# Find connection
$c = $m.EnumEveryConnection |? { $m.NetConnectionProps.Invoke($_).Name -eq "Ethernet" }

# Get sharing configuration
$config = $m.INetSharingConfigurationForINetConnection.Invoke($c)

# See if sharing is enabled
Write-Output $config.SharingEnabled

# See the role of connection in sharing
# 0 - public, 1 - private
# Only meaningful if SharingEnabled is True
Write-Output $config.SharingType

# Disable sharing
$config.DisableSharing()

# Enable sharing (0 - public, 1 - private)
$config.EnableSharing(0)