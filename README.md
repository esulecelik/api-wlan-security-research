# api-wlan-security-research

Backend API for WLAN/network attack demonstrations.

> ⚠️ For educational and research purposes only.  
> Unauthorized use is illegal. Use only on networks you own  or have explicit permission to test.

### Requirement
 
A monitor mode network adapter is required to craft network packets. 


### Endpoints

#### `POST /api/wlan/deauth/`

**Description:** Initiates a deauthentication attack against a target access point.

**Request Body (JSON):**
- `ssid` (string, required): Target AP BSSID (MAC address).
- `client-mac` (string, optional): Target client MAC address (if omitted, broadcast to all clients).
- `nic` (string, required): Monitor-mode network interface to use (e.g., `wlan0mon`).
- `attack-duration` (number, optional): Attack duration in seconds (default: `60`).

**Response:**
- `200 OK`: `{"message": "Deauth attack initiated successfully."}`
- `400 Bad Request`: `{"error": "..."}` (missing/invalid parameters or execution failure)

> ⚠️ Deauthentication attacks may be mitigated or blocked by WPA2 with 802.11w (Protected Management Frames) and WPA3.
 