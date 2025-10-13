import phonenumbers
from phonenumbers import geocoder
import time
import random

def start_phone_tracer(target):
    print(f"[+] PhoneTracer v2.1 - OSINT")
    print(f"[*] Target: {target}")
    print(f"[*] Initiating trace ...")

    p = phonenumbers.parse(target, None)
    r = geocoder.description_for_number(p, "en")

    print(f"[+] Location: {r}")
    print(f"[+] Trace complete")

# Call the function
start_phone_tracer("+91 9048682360")
