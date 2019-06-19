#!/usr/bin/python3
import paramiko
import os


def commandtoissue(command_to_issue,sshsession):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

def main():
    sshsession = paramiko.SSHClient()
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")
    sshsession.connect(hostname = "10.10.2.3", username="bender", pkey=mykey)
    

#   mycoomand=['touch sshworked.txt', 'ls']

#   for command in mycommands:
#       output = commandtoissue(command, sshsession)
#       print(output)

    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command('touch sshworked.txt')
    print(ssh_stdout.read())
   
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command('ls')
    print(ssh_stdout.read())
   
    session.close()

    print(help(sshsession.connect))

main()
