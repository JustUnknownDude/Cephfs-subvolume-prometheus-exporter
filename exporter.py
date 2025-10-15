import prometheus_client
import subprocess
import json
import time
from prometheus_client import Gauge, start_http_server
import threading

CEPH_VOLUMES = ["kubernetes-dev", "prod"]  # список CephFS volumes
CEPH_GROUPS = ["", "csi"] # Если группы не используются(_nogroup) оставляем только "" / If the group was not used (_nogroup), leave only ""
EXPORTER_PORT = 9109  #  prometheus port
SCRAPE_INTERVAL = 60

# Метрики
subvol_used_bytes = Gauge('cephfs_subvolume_used_bytes',
                          'Used bytes in CephFS subvolume',
                          ['volume', 'subvolume'])
subvol_quota_bytes = Gauge('cephfs_subvolume_quota_bytes',
                           'Quota (max bytes) of CephFS subvolume',
                           ['volume', 'subvolume'])
subvol_free_bytes = Gauge('cephfs_subvolume_free_bytes',
                          'Free bytes in CephFS subvolume',
                          ['volume', 'subvolume'])

# Отключаем ненужные коллекторы
prometheus_client.REGISTRY.unregister(prometheus_client.PROCESS_COLLECTOR)
prometheus_client.REGISTRY.unregister(prometheus_client.PLATFORM_COLLECTOR)
prometheus_client.REGISTRY.unregister(prometheus_client.GC_COLLECTOR)

def run_ceph_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Ошибка выполнения команды: {cmd}\n{e.stderr}")
        return None
    except json.JSONDecodeError:
        print(f"[ERROR] Не удалось распарсить JSON: {cmd}")
        return None


def collect_metrics():
    for volume in CEPH_VOLUMES:
      for group in CEPH_GROUPS:
        subvolumes = run_ceph_cmd(f"ceph fs subvolume ls {volume} {group} --format json")
        if not subvolumes:
            continue

        for sub in subvolumes:
            sub_name = sub.get("name")
            if not sub_name:
                continue

            info = run_ceph_cmd(f"ceph fs subvolume info {volume} {sub_name} {group} --format json")
            if not info:
                continue

            used_bytes = info.get("bytes_used", 0)
            quota_bytes = info.get("bytes_quota", 0)
            free_bytes = max(quota_bytes - used_bytes, 0) if quota_bytes > 0 else 0

            subvol_used_bytes.labels(volume, sub_name).set(used_bytes)
            subvol_quota_bytes.labels(volume, sub_name).set(quota_bytes)
            subvol_free_bytes.labels(volume, sub_name).set(free_bytes)

            print(f"[OK] {volume}/{sub_name}: used={used_bytes}, quota={quota_bytes}, free={free_bytes}")


if __name__ == "__main__":
    start_http_server(EXPORTER_PORT)
    while True:
        collect_metrics()
        time.sleep(SCRAPE_INTERVAL)
