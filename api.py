import cdb_id
import requests
import os
import time

# Request limit. YGOProDeck has a request limit of 20 per 1 second.
REQUESTS_PER_SECOND = 18
REQUEST_INTERVAL = 1.0 / REQUESTS_PER_SECOND

#*================================================================

def download(path, all_cards):
    card_ids = cdb_id.idlist(path, all_cards) # list of all card IDs
    
    if not card_ids:
        print("Error: Wrong directory") # exits if list is empty
        return
    
    save_dir = path + "/pics"

    for card_id in card_ids:
        image_url = f"https://images.ygoprodeck.com/images/cards/{card_id}.jpg"
        local_filename = os.path.join(save_dir, f"{card_id}.jpg")

        if not os.path.exists(local_filename): # if the image does not exist
            try:
                card_image = requests.get(image_url)
                card_image.raise_for_status()  # Check for HTTP errors

                with open(local_filename, "wb") as f:
                    f.write(card_image.content)
                print(f"Downloaded: {local_filename}")
            except requests.exceptions.RequestException as e:
                print(f"Error downloading {card_id}: {e}")

        time.sleep(REQUEST_INTERVAL)