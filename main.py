import requests
from datetime import datetime, timedelta
from tkinter import *

USER_NAME = "tubbietoaster"
TOKEN = "baasoi393hrie092ee8f"
GRAPH_ID = "graph12121"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

today = datetime.now() - timedelta(days=1)
yesterday_formatted = today.strftime("%Y%m%d")
print(yesterday_formatted)

#'+++++++++CREATE NEW USER ACCOUNT ON PIXELA++++++++++++++++#

# response = requests.post(url = pixela_endpoint, json=user_params)
# print(response.text)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#++++++++++++++++++CREATE A GRAPH++++++++++++++++++++#

# graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
#
graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "ajisai",

}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#+++++++++++++++++++++++++++++++++++++++++++++++++++#

#++++++++++++++++++POST A VALUE TO THE GRAPH+++++++++# ---> IMPORTANT PART!!!!
def upload_data():
    value_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
    #pages_read = input("How many pages did you read today? ")

    value_config = {
        "date": yesterday_formatted,
        "quantity": str(pages_read.get()),
    }


    response = requests.post(url=value_endpoint, json=value_config, headers=headers)
    #print(response.text)
    #print(type(response.text))
    # {"message":"Success.","isSuccess":true}
    if response.text == '{"message":"Success.","isSuccess":true}':
         label_status.config(text="✅")
    else:
         label_status.config(text="⛔️")
#+++++++++++++++++++++++++++++++++++++++++++++++++++#

#+++++++++++++++++++UPDATE A PIXEL+++++++++++++++++++#
def update_data():
    update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{yesterday_formatted}"

    update_config = {
        "quantity": str(pages_read.get()),
    }

    update = requests.put(url=update_endpoint, json=update_config, headers=headers)
    print(update.text)
    #{"message":"Success.","isSuccess":true}
    if update.text == '{"message":"Success.","isSuccess":true}':
        label_status.config(text="✅")
    else:
        label_status.config(text="⛔️")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#++++++++++++++++++DELETE A PIXEL++++++++++++++++++++++#
# delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{yesterday_formatted}"

# delete = requests.delete(url=delete_endpoint, headers=headers)
# print(delete.text)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++

#+++++++++++++++CREATE GUI++++++++++++++++++++++++++++
window = Tk()

window.title("Reading Habit Tracker")
window.config(bg="#D6EFED", padx=50, pady=50)

#picture
canvas = Canvas(width=550, height=400, bg="#D6EFED", highlightthickness=0)
book_img = PhotoImage(file="book.png")
canvas.create_image(275, 200, image=book_img)
timer_text = canvas.create_text(275, 150, text="How many pages did you read yesterday?",
                                font=("Arial", 20, "bold"), fill="#614124")
canvas.grid(row=1, column=1)

#input
pages_read = Spinbox(width=5, from_=1, to=2000)
pages_read.grid(row=2, column=1)

# buttons
upload_button = Button(text="Submit", highlightthickness=0, command=upload_data)
upload_button.grid(row=3, column=0)

update_button = Button(text="Update", highlightthickness=0, command=update_data)
update_button.grid(row=3, column=2)

#Labels
label_status = Label(text="")
label_status.grid(row=3, column=1)


window.mainloop()










