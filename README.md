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

3. In the exporter.py file, you need to specify the names of your volumes in cephfs for which you need metrics, for example:\
   CEPH_VOLUMES = ["kubernetes-dev", "prod", "dev"]\
   If you use groups, you need to specify them:\
   CEPH_GROUPS = ["", "csi"]\
   If you don't use groups (only _nogroup ) leave it like this:\
   CEPH_GROUPS = [""]

```
sudo nano /opt/subvolume-exporter/exporter.py
   ```
   
4. Enable the service
   
   ```
   systemctl daemon-reload && systemctl enable subvolume-exporter --now
   ```
   
5. Done. The exporter is running on port http://your_host_ip:9109

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

3. В файле exporter.py необходимо указать названия ваших volume в cephfs, по которым нужны метрики, например: \
CEPH_VOLUMES = ["kubernetes-dev", "prod", "dev"] \
Если вы используете группы, то их нужно указать: \
CEPH_GROUPS = ["", "csi"] \
Если вы не используете группы ( только _nogroup ) оставьте так: \
CEPH_GROUPS = [""]

```
sudo nano /opt/subvolume-exporter/exporter.py
```

4.    Включаем службу
   
   ``` 
   systemctl daemon-reload && systemctl enable subvolume-exporter --now
```
   
5.    Готово. Экспортер запущен на порту http://your_host_ip:9109
