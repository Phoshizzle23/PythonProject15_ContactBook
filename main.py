import PySimpleGUI as sg
import csv


def save_contact(values):
    fname = values['-fname-']
    lname = values['-lname-']
    phone = values['-phone-']
    email = values['-email-']
    address = values['-address-']
    info = [fname, lname, phone, email, address]

    with open('info.csv', 'a', newline="") as w:
        cw = csv.writer(w)
        cw.writerow(info)

    clear_input_fields()

def delete_contact(lname):
    with open('info.csv', 'r') as r:
        lines = r.readlines()

    with open('info.csv', 'w') as w:
        for line in lines:
            contact = line.strip().split(',')
            if contact[1] != lname:
                w.write(line)

def search_contact(values):
    searchText = values['-searchText-']
    found_contacts = []

    with open('info.csv', 'r') as r:
        cr = csv.reader(r)
        for i in cr:
            print("Current i:", i)  # Print the contents of the i list
            if len(i) >= 5 and i[1] == searchText:
                found_contacts.append(
                    [sg.Text(
                        f"First Name: {i[0]}\nLast Name: {i[1]}\nPhone Number: {i[2]}\nEmail: {i[3]}\nAddress: {i[4]}"),
                     sg.Button('Delete')])

    if found_contacts:
        # Display each found contact along with a "Delete" button
        window['-searchOutput-'].update(f"First Name: {i[0]}\nLast Name: {i[1]}\nPhone Number: {i[2]}\nEmail: {i[3]}\nAddress: {i[4]}")
    else:
        window['-searchOutput-'].update("No matching contacts found.")

def clear_input_fields():
    for key in ['-fname-', '-lname-', '-phone-', '-email-', '-address-']:
        window[key].update('')


def main():
    sg.theme('black')
    sg.set_options(font='Arial 16')

    layout = [
        [sg.Text('Enter First Name'), sg.Push(), sg.InputText(key='-fname-')],
        [sg.Text('Enter Last Name'), sg.Push(), sg.InputText(key='-lname-')],
        [sg.Text('Enter Phone Number'), sg.Push(), sg.InputText(key='-phone-')],
        [sg.Text('Enter Email'), sg.Push(), sg.InputText(key='-email-')],
        [sg.Text('Enter Address'), sg.Push(), sg.InputText(key='-address-')],
        [sg.Button('Save'), sg.Button('Cancel')],
        [sg.Text("Search by Last name"), sg.Push(), sg.InputText(key='-searchText-')],
        [sg.Button('Search')],
        [sg.Text(key='-searchOutput-', )],
        [sg.Text('Enter Last Name to Delete'), sg.Push(), sg.InputText(key='-lname-delete-')],
        [sg.Button('Delete')]

    ]

    global window
    window = sg.Window('Contact Book', layout, icon='favicon.ico')

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Save':
            save_contact(values)
        elif event == 'Search':
            search_contact(values)
        elif event == 'Delete':
            lname_to_delete = values['-lname-delete-']
            delete_contact(lname_to_delete)
            window['-searchOutput-'].update('')
            window['-lname-delete-'].update('')  # Clear input field after deletion

    window.close()


if __name__ == '__main__':
    main()
