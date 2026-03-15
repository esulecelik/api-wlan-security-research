import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from logic.wifi import WiFiAttackManager


class DeauthAttackView(APIView):
    
    def post(self, request):
        # Extract parameters from the request
        target_bssid = request.data.get("ssid")
        target_client_mac = request.data.get("client-mac")
        interface = request.data.get("nic")
        attack_duration = request.data.get("attack-duration", 60)  # Default to 60 seconds

        # Log the received parameters
        logging.info(f"Received deauth attack request: BSSID={target_bssid}, AP MAC={target_client_mac}, Duration={attack_duration}")

        # Validate parameters
        if not target_bssid:
            return Response({"error": "Target BSSID is required."}, status=400)

        logging.info(f"Performing deauth attack on BSSID {target_bssid} for {attack_duration} seconds.")
        manager = WiFiAttackManager(interface)
        status = manager.deauth_attack(target_bssid, target_client_mac, attack_duration)
        
        if status:
            logging.info("Deauth attack initiated successfully.")
            return Response({"message": "Deauth attack initiated successfully."}, status=200) 

        return Response({"message": "Failed to initiate deauth attack."}, status=400)