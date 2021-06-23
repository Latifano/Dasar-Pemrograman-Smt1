import Globals


def CheckOnOff():
    return Globals.g_onoff


def TurnOnOff():
    global CheckOnOff
    CheckOnOff = True
    if CheckOnOff is True:
        Globals.g_onoff = False
    else:
        Globals.g_onoff = True


def TempUp():
    if CheckOnOff is True:
        Globals.g_temp += 1
        if Globals.g_temp > 30:
            Globals.g_temp = 18


def TempDown():
    if CheckOnOff is True:
        Globals.g_temp -= 1


def FanSpeed():
    if CheckOnOff is True:
        Globals.g_fanlevel += 1
        if Globals.g_fanlevel > 4:
            Globals.g_fanlevel = 1


def Powerchill():
    if CheckOnOff is True:
        Globals.g_temp == 18 and Globals.g_fanlevel == 4


def Display():
    print('Temperatur suhu :', Globals.g_temp)
    print('Level kipas     :', Globals.g_fanlevel)
