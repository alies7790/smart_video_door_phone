import websocket
import _thread
import time
import rel
import ast
rel.safe_read()

def on_message(ws, message):
    massage1=ast.literal_eval(message)
    if(massage1["code"] == 1011):
        # request for open door
        pass
    elif massage1["code"] == 1012:
        # on detect and open with them
        pass
    elif massage1["code"] == 1013:
        # off detect and open with them
        pass
    elif massage1["code"] == 1014:
        # add new member
        idMember=massage1["id_member"]
        pass
    elif massage1["code"] == 1015:
        # update member
        idMember = massage1["id_member"]
        pass
    elif massage1["code"] == 1016:
        # OK
        pass

    print(massage1["code"])
    print(massage1["massege"])



def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")

if __name__ == "__main__":
    header={'token':'12345', 'serial-rasperypi':'1234567891234567'}
    ws = websocket.WebSocketApp("wss://smartvideodoorphoneproject.herokuapp.com/ws/open_door_websocket/",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                                on_close=on_close,
                                header=header
                                )

    ws.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()
