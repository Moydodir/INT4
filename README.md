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
### Fail2Ban: Protects the server from brute-force attacks by banning IPs based on configured rules.
**Default Variables**

1. bantime: Duration (in seconds) for which an IP address will be banned (default: `600`).
2. findtime: Time frame (in seconds) during which failed login attempts are counted (default: `600`).
3. maxretry: Maximum number of allowed failed login attempts before banning (default: `5`).

**Tasks Overview**

1. **Install necessary packages**: Installs `rsyslog` and `iptables` for logging and firewall management.
2. **Configure logging**: Sets up SSH logging and ensures the log directory exists.
3. **Install Fail2Ban**: Installs the Fail2Ban package and configures it.

**Configuration Template**

The role utilizes a Jinja2 template (`jail.local.j2`) for Fail2Ban's configuration, which is dynamically populated with the defined variables.

### UFW: Simplifies firewall management for the server, allowing or denying incoming connections.
1. Set default outgoing policy to allow: Configures UFW to allow all outgoing connections by default.
2. Allow SSH connections: Opens port 22 for SSH, enabling remote access to the server.

