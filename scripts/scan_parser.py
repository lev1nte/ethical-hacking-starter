#!/usr/bin/env python3
"""
scan_parser.py
Safe nmap XML -> CSV summary parser for lab use only.
Usage:
  python3 scan_parser.py --input sample_scan.xml --output summary.csv
"""

import argparse
import csv
import xml.etree.ElementTree as ET

def parse_nmap_xml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    results = []
    for host in root.findall('host'):
        addr = host.find('address').attrib.get('addr', 'unknown')
        hostname_tag = host.find('hostnames/hostname')
        hostname = hostname_tag.attrib.get('name') if hostname_tag is not None else ''
        for port in host.findall('.//port'):
            portid = port.attrib.get('portid')
            proto = port.attrib.get('protocol')
            state = port.find('state').attrib.get('state')
            service_tag = port.find('service')
            service = service_tag.attrib.get('name') if service_tag is not None else ''
            results.append({
                'ip': addr,
                'hostname': hostname,
                'protocol': proto,
                'port': portid,
                'state': state,
                'service': service
            })
    return results

def write_csv(results, out_path):
    keys = ['ip','hostname','protocol','port','state','service']
    with open(out_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for r in results:
            writer.writerow(r)

def main():
    parser = argparse.ArgumentParser(description='Parse nmap XML (lab-only) to CSV summary.')
    parser.add_argument('--input', required=True, help='nmap XML file (lab-only)')
    parser.add_argument('--output', default='summary.csv', help='output CSV filename')
    args = parser.parse_args()

    results = parse_nmap_xml(args.input)
    write_csv(results, args.output)
    print(f'Parsed {len(results)} entries. Output saved to {args.output}')

if __name__ == '__main__':
    main()
