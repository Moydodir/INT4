# Debian 11 Server Configuration

This project contains Ansible configurations for setting up a Debian 11 server, including the installation and configuration of PostgreSQL 16, UFW (Uncomplicated Firewall), and Fail2Ban for enhanced security.

## Project Structure

<pre>
ansible  
├── ansible.cfg
├── ansible-playbook.yml 
├── hosts
├── roles
│   └── setup
│       ├── fail2ban
│       │   ├── defaults
│       │   │   └── main.yml
│       │   ├── handlers
│       │   │   └── main.yml 
│       │   ├── meta
│       │   │   └── main.yml
│       │   ├── tasks
│       │   │   └── main.yml
│       │   ├── templates
│       │   │   └── jail.local.j2
│       │   └── tests
│       │       ├── inventory
│       │       └── test.yml
│       └── ufw
│           ├── meta
│           │   └── main.yml
│           ├── tasks
│           │   └── main.yml
│           └── tests
│               ├── inventory
│               └── test.yml
└── vars.yml
</pre>


## Getting Started

1. **Install Ansible** on your control machine:
   ```bash
   sudo apt update
   sudo apt install ansible
2. **Configure the Inventory**:
    Update the hosts file with your target server details, install ssh server on it and create user 'ansible' with NOPASSWD rule in sudoers.
3. **Run the Playbook**:
   ansible-playbook -i hosts ansible-playbook.yml

## Roles
**Fail2Ban**: Protects the server from brute-force attacks by banning IPs based on configured rules.
**UFW**: Simplifies firewall management for the server, allowing or denying incoming connections.

