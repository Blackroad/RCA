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
                    print (result_state,"\nRecieved Data:", result_data_name,"\x1b[1;32m""\n")
                    confirm = input(
                        'Select test case for executing:  \n1 - T-006 Disposition actions (e-sign)'
                        '\n2 - T-010-012 Submit failure event'
                        '\n3 - T-014 Rework NCP loop'
                        '\nInput number(1,2,3) and click ENTER:  ')
                    if int(confirm) == 1:
                        pytest.main(['T-006_Dispositon_actions(e-sign).py'])
                    elif int(confirm) == 2:
                        pytest.main(['T-010-012_Submit_failure_events.py'])
                    elif int(confirm) == 3:
                        pytest.main(['T-014_Rework_NCP.py'])
                    else:
                        continue

                elif result[1] == state[1]:
                     result_state = '\nUser Card status: Card not Initialized'
                     result_message = result[3:]
                     print (result_state,'\n'+ "Reason is:" + ' '+(' '.join([i for i in result_message])),"\x1b[1;32m")
                     if input('Do you want to run appropriate test(Y/N):  ') == 'Y':
                         pytest.main(["--html=report.html",'T-008_Disposition_actions_without_card.py'])
                     else:
                         continue

                elif result[1] == state[2]:
                     result_state = '\nUser Card status: Card not Initialized'
                     result_message = result[3:]
                     print(result_state, '\n' + "Reason is:" + ' ' + (' '.join([i for i in result_message])),"\x1b[1;32m")
                     if input('Do you want to run appropriate test(Y/N):  ') == 'Y':
                         pytest.main(['T-009_Disposition_actions_with_incorrect_card.py'])
                     else:
                         continue

                elif state[3]:
                     result_state = '\nUser Card status: Card not Initialized'
                     result_message = result[3:]
                     print(result_state, '\n' + "Reason is:" + ' ' + (' '.join([i for i in result_message])),"\x1b[1;32m")
                     if input('Do you want to run appropriate test(Y/N):  ') == 'Y':
                         pytest.main(['T-007_Dispositon_actions_without_card_reader.py'])
                     else:
                         continue
    except OSError:
        print("\x1b[1;31m", '\nService is not started!\n',"\x1b[1;32m")
        if input('Do you want to run appropriate test(Y/N):  ') == 'Y':
            pytest.main(['T-013_Disposition_actions(serviceOFF).py'])
            print('\nStart service to perform testing with card reader data')







def run_webclient(Card_Reader_thread):
    asyncio.get_event_loop().run_until_complete(Card_Reader_thread())

colorama.init()

run_webclient(Card_Reader_thread)
