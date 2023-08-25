from bose.launch_tasks import launch_tasks
from bose import LocalStorage
from src import tasks_to_be_run

msg = '''
Google Maps Leads have been successfully scraped! 
This code is being Developed by Niladri Ghoshal. please give me a Star ⭐ in my GitHub repository by clicking:
https://github.com/niladrighoshal/scrap_googleMaps 

'''

def print_pro_bot():
    global msg
    print(msg) 

if __name__ == "__main__":

    launch_tasks(*tasks_to_be_run)
    count = LocalStorage.get_item('count', 0)
    
    print_pro_bot()
