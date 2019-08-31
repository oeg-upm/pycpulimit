import sys
import subprocess
import psutil
import argparse



def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    # Iterate over the all the running process
    print("searching for process: %s" % processName)
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                print("process_id: %d" % proc.pid)
                # return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;


def limit(pname, total_limit):
    print("searching for process: %s" % pname)
    pids = []
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if pname.lower() in proc.name().lower():
                print("process_id: %d" % proc.pid)
                pids.append(proc.pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    if pids == []:
        print("Could not find a process with the name <%s>" % (pname))
        print('Try this command: ps -ef | grep "%s" ' % pname)
    else:
        limit_per_process = total_limit/len(pids)
        for pid in pids:
            comm = "cpulimit --limit=%d --pid=%d" % (limit_per_process, pid)
            print(comm)
            subprocess.Popen(comm, shell=True)
        print("All the processes with the name %s has been limited" % pname)


def cmd():
    parser = argparse.ArgumentParser(description='Limit processes by name')
    parser.add_argument('name', help='A segment of the name of the process')
    parser.add_argument('limit', type=int, help='The total limit of the processes with the given name')
    args = parser.parse_args()
    limit(args.name, args.limit)


if __name__ == "__main__":
    cmd()
