import platform
import psutil
import time
import os

def to_gb(bytes):
    result = bytes / 1024 / 1024 / 1024
    return result

def get_ram_info():
    ram = psutil.virtual_memory()
    ram_gb = to_gb(ram.total)
    
    return ram_gb, ram.percent

def get_disk_info():
    disk = psutil.disk_usage("C:\\")
    disk_total = to_gb(disk.total)
    disk_used = to_gb(disk.used)
    disk_free = to_gb(disk.free)
    disk_percent = disk.percent
    
    return disk_total, disk_used, disk_free, disk_percent

def get_cpu_data():
    cpu_data = {}
    
    for process in psutil.process_iter():
        cpu = process.cpu_percent()
        cpu_data [process.pid] = cpu
                    
    time.sleep(1)
    
    process_data = {}
    
    for process in psutil.process_iter():
        cpu = process.cpu_percent()
        process_data [process.pid] = process.name(), cpu
            
    sorted_processes = sorted(
        process_data.items(),
        key=lambda x: x[1][1],
        reverse=True
    )
    
    for pid, (name, cpu) in sorted_processes[:10]:
        if name == "System Idle Process":
            continue
        print(name, "|", "PID:", pid, "|", "CPU:", cpu, "%")
        
    return cpu_data
        
while True:
    os.system("cls")
    
    disk_total, disk_used, disk_free, disk_percent = get_disk_info()
    
    cpu_usage = psutil.cpu_percent()
    
    ram_gb, ram_percent = get_ram_info()
    
    print("================================")
    print("        MY PC MONITOR")
    print("================================")
    print("Операционная система: ", platform.system())
    print("Диск С:", "Всего: ", round(disk_total, 1), "GB", "|", 
        "Занято: ", round(disk_used,1), "GB", "|", 
        "Свободно: ", round(disk_free,1), "GB", "|",
        "Использовано: ", disk_percent, "%")
    print("Процессор: ", platform.processor())
    print("Архитектура: ", platform.machine())   
    print("Загрузка процессора: ", cpu_usage, "%")
    print("Оперативная память:", round(ram_gb,1), "GB", "|", ram_percent, "%")
    
    cpu_data = get_cpu_data()
    
    time.sleep(1)
    
