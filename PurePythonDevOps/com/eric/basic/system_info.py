'''
文件主要用来演示如何获取系统的相关信息
'''
from time import sleep
import psutil

__author__ = 'Eric'


# 获取内存信息
def memory_info():
    virtual_mem = psutil.virtual_memory();
    swap_mem = psutil.swap_memory();
    print_message("virtual_mem:", virtual_mem)
    print_message("swap_memory:", swap_mem)


#获取CPU信息
def cpu_info():
    cpu_count = psutil.cpu_count;
    cpu_times = psutil.cpu_times();
    cpu_percent = psutil.cpu_percent();
    print_message("cpu_count", cpu_count)
    print_message("cpu_times", cpu_times)
    print_message("cpu_percent", cpu_percent)

#模糊匹配查找指定的进程，找到对应的进程会将其终止，然后再答应出所有进程的信息
def terminal_process_by_name(process_name):
    pidList = psutil.pids();
    found_target_process=False
    for eachPid in pidList:
        try:
            eachProcess = psutil.Process(eachPid);
            processName = eachProcess.name;
            if (str(processName).lower().find( str(process_name).lower())>0):
                found_target_process=True
                print("Found process");
                print("processName=", processName);
                processExe = eachProcess.exe;
                print("processExe=", processExe);
                processGetcwd = eachProcess.cwd();
                print("processGetcwd=", processGetcwd);
                processCmdline = eachProcess.cmdline;
                print("processCmdline=", processCmdline);
                processStatus = eachProcess.status;
                print("processStatus=", processStatus);
                processUsername = eachProcess.username;
                print("processUsername=", processUsername);
                processCreateTime = eachProcess.create_time;
                print("processCreateTime=", processCreateTime);
                print("Now will terminate this process !");
                print("终止目标进程！")
                eachProcess.terminate();
                eachProcess.wait(timeout=3);
                print("最新进程列表！")
                print("psutil.test()=", psutil.test());

        except psutil.NoSuchProcess as pid:
            print("no process found with pid="+pid);

    if not found_target_process:
        print("进程："+process_name+" 没有发现")


def print_network():
    network_informations = psutil.net_if_addrs()
    print_message("NetworkInfo:", network_informations)
    # for network_interface in network_informations:
    #     print(network_interface);


def print_message(key='', value=None):
    print(key + str(value))


if __name__ == "__main__":
    while True:
        print("#########################################")
        terminal_process_by_name("notepad")
        # print_network()
        # memory_info()
        # cpu_info()
        sleep(2);


