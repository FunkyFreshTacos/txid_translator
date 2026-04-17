# Translate the TXID for various sensors for Risco
def translate_txid(txid, insert_val, prefix, threshold=5):
    hex_txid = hex(txid)
    payload_len = len(hex_txid) - 2
    
    if payload_len < threshold:
        # For small values, insert value + '0'
        new_hex = hex_txid[:2] + str(insert_val) + '0' + hex_txid[2:]
    else:
        # For large values, just insert value
        new_hex = hex_txid[:2] + str(insert_val) + hex_txid[2:]
    
    translated = str(int(new_hex, 16))
    final_txid = prefix + translated
    print(f"Translated TXID:  {final_txid} \n\n")

# Configuration for sensors: (insert_val, prefix, threshold)
# NOTE: KEY2_PANIC1 and TILT1 have special logic and are handled via dedicated functions.

# KEY2_PANIC1 has a weird branch in original:
# elif len(txid)-2 >= 6:
#     txid = "".join(('048', txid)) # notice '048' instead of '0480'

# TILT1 also has a weird branch:
# elif len(txid)-2 >= 5:
#     txid = "".join(('112', txid)) # notice '112' instead of '1120'

def DW10_Magnet(txid): translate_txid(txid, 2, '0160')
def DW10_External(txid): translate_txid(txid, 2, '1120')
def SMKT3(txid): translate_txid(txid, 1, '1120')
def SMKT3_Heat(txid): translate_txid(txid, 9, '1120')
def SMKT3_Freeze(txid): translate_txid(txid, 8, '1120')
def GB1(txid): translate_txid(txid, 5, '0160')
def PIR1(txid): translate_txid(txid, 0, '0160')
def FT1(txid): translate_txid(txid, 4, '1120')
def FT1_Heat(txid): translate_txid(txid, 9, '1120')
def FT1_Freeze(txid): translate_txid(txid, 8, '1120')
def CO3(txid): translate_txid(txid, 7, '1120')
def HW_SHOCK(txid): translate_txid(txid, 3, '1120')

def KEY2_PANIC1(txid):
    hex_txid = hex(txid)
    if len(hex_txid) - 2 < 6:
        new_hex = hex_txid[:2] + '00' + hex_txid[2:]
        prefix = '0480'
    else:
        new_hex = hex_txid[:2] + '0' + hex_txid[2:]
        prefix = '048'
    translated = str(int(new_hex, 16))
    print(f"Translated TXID:  {prefix + translated} \n\n")

def TILT1(txid):
    hex_txid = hex(txid)
    if len(hex_txid) - 2 < 5:
        new_hex = hex_txid[:2] + 'C0' + hex_txid[2:]
        prefix = '1120'
    else:
        new_hex = hex_txid[:2] + 'C' + hex_txid[2:]
        prefix = '112'
    translated = str(int(new_hex, 16))
    print(f"Translated TXID:  {prefix + translated} \n\n")

def errhandler():
    print("Thats incorrect input. Try again: ")

def get_input():
    print("\nChoose which sensor you would like to have the TXID translated for:")
    print("-" * 68)
    sensors = [
        "DW10 Magnet", "DW10 External", "SMKT3", "SMKT3 - Heat", "SMKT3 - Freeze",
        "GB1-1", "PIR-1", "KEY-2, PANIC-1", "FT-1", "FT-1 - Heat", "FT-1 - Freeze",
        "CO3", "TILT1", "Honeywell Shock Sensors"
    ]
    for i, name in enumerate(sensors, 1):
        print(f"{i}. {name}")
    
    try:
        value = int(input("Enter a choice: "))
        if 1 <= value <= 14:
            return value
    except ValueError:
        pass
    
    print("Exiting... \n")
    quit()

def main():
    value = get_input()
    txid_input = input("Enter the TXID value: ")
    if len(txid_input) != 7:
        print("You gotta enter 7 digits for the TXID. ")
        return main()
    
    try:
        txid = int(txid_input)
        actions = {
            1: DW10_Magnet, 2: DW10_External, 3: SMKT3, 4: SMKT3_Heat, 5: SMKT3_Freeze,
            6: GB1, 7: PIR1, 8: KEY2_PANIC1, 9: FT1, 10: FT1_Heat, 11: FT1_Freeze,
            12: CO3, 13: TILT1, 14: HW_SHOCK
        }
        actions[value](txid)
    except ValueError:
        errhandler()
    except KeyError:
        errhandler()
    
    main()

if __name__ == "__main__":
    main()
