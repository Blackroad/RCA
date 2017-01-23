import asyncio
import websockets
import re
import pytest


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
                    print (result_state,"\nRecieved Data:", result_data_name)
                    if input('Do you want to run appropriate test(Y/N):  ') == 'Y':
                        if input('Do you want to make transition to "Disposition Complete" state(Y/N)?:  ') == 'Y':
                            pytest.main('test_units_submit_event.py')
                        else: pytest.main('test_units_serviceON_withCard.py')
                    else:
                        continue

                elif result[1] == state[1]:
                     result_state = '\nUser Card status: Card not Initialized'
                     result_message = result[3:]
                     print (result_state,'\n'+ "Reason is:" + ' '+(' '.join([i for i in result_message])))
                     if input('Do you want to run appropriate test(Y/N):  ') == 'Y':
                         pytest.main('test_units_serviceON_withoutCard.py')
                     else:
                         continue

                elif result[1] == state[2]:
                     result_state = '\nUser Card status: Card not Initialized'
                     result_message = result[3:]
                     print(result_state, '\n' + "Reason is:" + ' ' + (' '.join([i for i in result_message])))
                     if input('Do you want to run appropriate test(Y/N):  ') == 'Y':
                         pytest.main('test_units_serviceON_withoutCard.py')
                     else:
                         continue

                elif state[3]:
                     result_state = '\nUser Card status: Card not Initialized'
                     result_message = result[3:]
                     print(result_state, '\n' + "Reason is:" + ' ' + (' '.join([i for i in result_message])))
                     if input('Do you want to run appropriate test(Y/N):  ') == 'Y':
                         pytest.main('test_units_serviceON_withoutCardReader.py')
                     else:
                         continue
    except OSError:
        print('Service is not started!\nStart service and run script again')
        if input('Do you want to run appropriate test(Y/N):  ') == 'Y':
            pytest.main('test_units_serviceOFF.py')





def run_webclient(Card_Reader_thread):
    asyncio.get_event_loop().run_until_complete(Card_Reader_thread())


run_webclient(Card_Reader_thread)
