import logging
import re
from .cli.airodump import AirodumpScanner
from scapy.all import get_if_list
from typing import Optional


class WiFiAttackManager:
    
    interface:Optional[str] = None
    WIFI_PATTERN = re.compile(r'^(wlan\d+|wlp\d+s\d+(\w+)?|wlx[0-9a-f]{12}|wl\w+)$', re.IGNORECASE)

    def __init__(self,interface=None):
        self.interface=interface

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
        logging.info("Scanning for available Wi-Fi networks...")
        available_networks = AirodumpScanner.get_networks_in_range(interface)
        logging.info(f"Found {len(available_networks)} networks.")
        return available_networks
    
    def deauth_attack(self, target_bssid, target_client_mac=None, attack_duration=60)->Optional[bool]:
        logging.info(f"Initiating deauth attack on BSSID {target_bssid} for {attack_duration} seconds.")
        
        try:    
            airodump = AirodumpScanner()
            airodump.perform_deauth_attack(target_bssid, target_client_mac, attack_duration,self.interface)
            return True
        except Exception as e:
            logging.error(f"Error during deauth attack: {e}")
            return False
        
        