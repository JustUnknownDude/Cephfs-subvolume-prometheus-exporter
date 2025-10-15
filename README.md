# Cephfs subvolume prometheus exporter

## How to use

0. ```
   pip install prometheus_client
   ```

1. Copy exporter.py to /opt/subvolume-exporter/exporter.py
      
   ```
    sudo mkdir -p /opt/subvolume-exporter
   ```
   
   ```
   sudo curl -L https://raw.githubusercontent.com/JustUnknownDude/Cephfs-subvolume-prometheus-exporter/refs/heads/main/exporter.py -o /opt/subvolume-exporter/exporter.py && chmod +x /opt/subvolume-exporter/exporter.py
   ```

2. Copy subvolume-exporter.service to /etc/systemd/system/subvolume-exporter.service
   
   ```
   sudo curl -L https://raw.githubusercontent.com/JustUnknownDude/Cephfs-subvolume-prometheus-exporter/refs/heads/main/subvolume-exporter.service -o /etc/systemd/system/subvolume-exporter.service
   ```
3. Enable the service
   
   ```
   systemctl daemon-reload && systemctl enable subvolume-exporter --now
   ```
   
4. Done. The exporter is running on port http://your_host_ip:9109

## Как запустить

0. ```
   pip install prometheus_client
   ```

1.    Копируем exporter.py в /opt/subvolume-exporter/exporter.py
   
   ```
   sudo mkdir -p /opt/subvolume-exporter
```

   ```
   sudo curl -L https://raw.githubusercontent.com/JustUnknownDude/Cephfs-subvolume-prometheus-exporter/refs/heads/main/exporter.py -o /opt/subvolume-exporter/exporter.py && chmod +x /opt/subvolume-exporter/exporter.py
```

2.    Копируем subvolume-exporter.service в /etc/systemd/system/subvolume-exporter.service
   
   ```
   sudo curl -L https://raw.githubusercontent.com/JustUnknownDude/Cephfs-subvolume-prometheus-exporter/refs/heads/main/subvolume-exporter.service -o /etc/systemd/system/subvolume-exporter.service
```

3.    Включаем службу
   
   ``` 
   systemctl daemon-reload && systemctl enable subvolume-exporter --now
```
   
4.    Готово. Экспортер запущен на порту http://your_host_ip:9109
