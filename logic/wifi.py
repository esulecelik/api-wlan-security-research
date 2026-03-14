import logging
import re
from .cli.airodump import AirodumpScanner
from scapy.all import get_if_list
from typing import Optional


class WiFiAttackManager:
    
    WIFI_PATTERN = re.compile(r'^(wlan\d+|wlp\d+s\d+(\w+)?|wlx[0-9a-f]{12}|wl\w+)$', re.IGNORECASE)


    def list_wlan_interfaces(self)-> Optional[list]:
        '''
        Method to list available WLAN interfaces on the system.
        
        Returns:
            list|None: A list of WLAN interfaces or None if no interfaces are found.
        '''
        wireless_networks= [iface for iface in get_if_list() if self.WIFI_PATTERN.match(iface)]
        
        if not wireless_networks:
            logging.warning("No WLAN interfaces found on the system.")
            return None 
        
        return wireless_networks
        
    
    def list_available_networks(self, interface):
        # Placeholder for logic to scan and list available Wi-Fi networks
        logging.info("Scanning for available Wi-Fi networks...")
        # Simulate network scanning (replace with actual scanning code)
        available_networks = AirodumpScanner.get_networks_in_range(interface)
        logging.info(f"Found {len(available_networks)} networks.")
        return available_networks