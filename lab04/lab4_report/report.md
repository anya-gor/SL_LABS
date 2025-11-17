whoami; pwd; uname -a > files/1_info.txt
cat > ~/secret.txt
chmod go-rw ~/secret.txt
cat ~/secret.txt > files/secret_backup.md
chmod 755 files/secret_backup.md
mv ~/secret.txt files/
sudo chown root files/secret_backup.md
ls /etc/host* > files/8_etc_hosts.txt
find /var/log/ -type f -mtime -7 > files/9_recent_logs.txt
sudo useradd -m -s /bin/bash auditor
sudo usermod -aG sudo auditor
sudo passwd auditor
sudo su - auditor
cat > /home/auditor/audit_report.txt
chmod 666 /home/auditor/audit_report.txt
exit
sudo cp /home/auditor/audit_report.txt files/14_audit_report.txt
sudo userdel -r auditor
cat /etc/passwd > files/16_users.txt
grep -r "localhost" /etc/ 2>/dev/null > files/17_localhost_files.txt
find /usr/bin/ -type f -executable -user root > files/18_root_binaries.txt
find ~ -type f -size +1M > files/19_large_files.txt
mkdir test_search
cd test_search
echo "port=8080" > data1.conf
echo "debug=true" > data2.conf
touch readme.txt
cd ..
grep -rl "port\|debug" test_search/ > files/21_config_files.txt
find test_search/ -type f -empty -delete
sleep 1h &
ps -u $USER > files/24_my_processes.txt
pgrep sleep
pkill sleep
sudo apt update && sudo apt install htop
htop
ps aux | grep systemd > files/27_systemd_processes.txt
tail -20 /var/log/syslog > files/28_syslog_tail.txt
grep "failed" /var/log/auth.log > files/29_failed_logins.txt
dpkg -l > files/30_installed_packages.txt
ss -tuln > files/31_open_ports.txt
tar -czf lab4_files_backup.tar.gz files/
rm -rf files/
tar -xzf lab4_files_backup.tar.gz
cp -r lab4_report/ lab4_final/
rm -rf lab4_final/
tree . > files/36_tree.txt

