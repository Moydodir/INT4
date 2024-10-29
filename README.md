# Monitoring Configuration for Availability Metrics

This repository contains configuration files for setting up and collecting availability metrics for [PT Security](https://ptsecurity.com). 
The configurations are structured for use with monitoring tools to ensure reliable tracking and alerting on system health and uptime.

## Structure

The project includes the following files:

prometheus
├── blackbox.yml
└── prometheus.yml


### Files

- **`blackbox.yml`**: Configuration for the Blackbox Exporter, which is responsible for probing endpoints to monitor their availability.
  This file defines the probe settings, including target endpoints and probing intervals.

- **`prometheus.yml`**: Configuration for Prometheus, which scrapes metrics from the Blackbox Exporter and other sources.
  This file includes scrape settings, job definitions, and endpoint configurations for data collection.

## Usage

1. **Install Prometheus and Blackbox Exporter**. You can find installation guides and binaries on their respective
   [Prometheus](https://prometheus.io/docs/prometheus/latest/installation/),
   [Install Prometheus on Debian 11](https://vegastack.com/tutorials/how-to-install-prometheus-on-debian-11/)
   and
   [Blackbox Exporter](https://github.com/prometheus/blackbox_exporter) websites.

3. **Place the configuration files** in the appropriate directories for Prometheus and the Blackbox Exporter:
   - `blackbox.yml`: Should be placed in the Blackbox Exporter’s configuration directory.
   - `prometheus.yml`: Should be placed in Prometheus’s configuration directory (usually `/etc/prometheus/`).

4. **Start or reload Prometheus and Blackbox Exporter**:
   - Restart the services or reload their configurations to apply the new settings:
     ```bash
     # For Prometheus
     systemctl restart prometheus

     # For Blackbox Exporter
     systemctl restart blackbox_exporter
     ```

## Monitoring Setup

Once set up, Prometheus will scrape metrics from the Blackbox Exporter according to the specified configuration, gathering availability data on [PT Security’s](https://ptsecurity.com) endpoints.
The gathered metrics will help you monitor uptime and diagnose connectivity issues.

## Additional Resources

- [Prometheus Documentation](https://prometheus.io/docs/introduction/overview/)
- [Blackbox Exporter Documentation](https://github.com/prometheus/blackbox_exporter)
- [PT Security Website](https://ptsecurity.com)
