import asyncio
import websockets
import re
import pytest
import time
import colorama


async def Card_Reader_thread():
    try:
        async with websockets.connect('ws://localhost:4000') as websocket:
            while True:
                message = await websocket.recv()
                state = ["0", "1609561978", "1609562107", "-2146435049"]
                result = re.findall(r'\w+', message)
                if  result[1] == state[0]:
                    result_state = '\nUser Card status: Card is initialized'
                    result_data_name = '\nUser First Name / Last Name : {} {}\nUserlogin : {}\nUser ID : {}'.format(result[4], result [6], result [8], result [10])
                    print (result_state,"\nRecieved Data:", result_data_name,"\x1b[1;32m")
                    confirm = input(
                        'Select test case for executing:  \n1 - Check usual data receiving through card reader'
                        '\n2 - Check unit transition to "Disposition Complete" state'
                        '\n3 - Check NCP loop for REWORK item'
                        '\nInput number(1,2,3) and click ENTER:  ')
                    if int(confirm) == 1:
                        pytest.main(['test_units_serviceON_withCard.py'])
                    elif int(confirm) == 2:
                        pytest.main(['test_units_submit_event.py'])
                    elif int(confirm) == 3:
                        pytest.main(['test_rework_NCP.py'])


                elif result[1] == state[1]:
                     result_state = '\nUser Card status: Card not Initialized'
                     result_message = result[3:]
                     print (result_state,'\n'+ "Reason is:" + ' '+(' '.join([i for i in result_message])),"\x1b[1;32m")
                     if input('Do you want to run appropriate test(Y/N):  ') == 'Y':
                         pytest.main(['test_units_serviceON_withoutCard.py'])
                     else:
                         continue

                elif result[1] == state[2]:
                     result_state = '\nUser Card status: Card not Initialized'
                     result_message = result[3:]
                     print(result_state, '\n' + "Reason is:" + ' ' + (' '.join([i for i in result_message])),"\x1b[1;32m")
                     if input('Do you want to run appropriate test(Y/N):  ') == 'Y':
                         pytest.main(['test_units_serviceON_withoutCard.py'])
                     else:
                         continue

                elif state[3]:
                     result_state = '\nUser Card status: Card not Initialized'
                     result_message = result[3:]
                     print(result_state, '\n' + "Reason is:" + ' ' + (' '.join([i for i in result_message])),"\x1b[1;32m")
                     if input('Do you want to run appropriate test(Y/N):  ') == 'Y':
                         pytest.main(['test_units_serviceON_withoutCardReader.py'])
                     else:
                         continue
    except OSError:
        print("\x1b[1;31m", '\nService is not started!\n',"\x1b[1;32m")
        if input('Do you want to run appropriate test(Y/N):  ') == 'Y':
            pytest.main(['test_units_serviceOFF.py'])
            print('\nStart service to perform testing with card reader data')







def run_webclient(Card_Reader_thread):
    asyncio.get_event_loop().run_until_complete(Card_Reader_thread())

colorama.init()

run_webclient(Card_Reader_thread)
