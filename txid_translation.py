#Translate the TXID for the DW-10 external loop Final TXID for Risco
def DW10_External( txid ):
    txid = hex(txid)
    if len(txid)-2 < 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '20' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('1120', txid))
        print "Translated TXID: ",txid, "\n\n"
    elif len(txid)-2 >= 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '2' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('1120', txid))
        print "Translated TXID: ",txid, "\n\n"
    else:
        print "Got a false value!"


#Translate the TXID for the DW-10 magnet loop for the Final TXID for Risco
def DW10_Magnet( txid ):
    txid = hex(txid)
    if len(txid)-2 < 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '20' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('0160', txid))
        print "Translated TXID: ",txid, "\n\n"
    elif len(txid)-2 >= 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '2' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('0160', txid))
        print "Translated TXID: ",txid, "\n\n"
    else:
        print "Got a false value!"    
    

#Translate the TXID for the SMKT3 to the Final TXID for Risco
def SMKT3( txid ):
    txid = hex(txid)
    if len(txid)-2 < 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '10' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('1120', txid))
        print "Translated TXID: ",txid, "\n\n"
    elif len(txid)-2 >= 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '1' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('1120', txid))
        print "Translated TXID: ",txid, "\n\n"
    else:
        print "Got a false value!"
    

#Translate the TXID for the GB1 to the Final TXID for Risco
def GB1( txid ):
    txid = hex(txid)
    if len(txid)-2 < 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '50' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('0160', txid))
        print "Translated TXID: ",txid, "\n\n"      
    elif len(txid)-2 >= 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '5' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('0160', txid))
        print "Translated TXID: ",txid, "\n\n"     
    else:
        print("Got a false value!")
    



#Translate the TXID for the PIR to the Final TXID for Risco
def PIR1( txid ):
    txid = hex(txid)
    if len(txid)-2 < 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '00' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('0160', txid))
        print "Translated TXID: ",txid, "\n\n"     
    elif len(txid)-2 >= 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '0' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('0160', txid))
        print "Translated TXID: ",txid, "\n\n"     
    else:
        print("Got a false value!")
    



#Translate the TXID for the key2 and panic to the Final TXID for Risco
def KEY2_PANIC1( txid ):
    txid = hex(txid)
    if len(txid)-2 < 6:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '00' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('0480', txid))
        print "Translated TXID: ",txid, "\n\n"     
    elif len(txid)-2 >= 6:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '0' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('048', txid))
        print "Translated TXID: ",txid, "\n\n"     
    else:
        print("Got a false value!")    
    



#Translate the TXID for the FT1 to the Final TXID for Risco
def FT1( txid ):
    txid = hex(txid)
    if len(txid)-2 < 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '40' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('1120', txid))
        print "Translated TXID: ",txid, "\n\n"     
    elif len(txid)-2 >= 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '4' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('1120', txid))
        print "Translated TXID: ",txid, "\n\n"     
    else:
        print("Got a false value!")    


#Translate the TXID for the SMKT3 Heat with heat loop to the Final TXID for Risco
def SMKT3_Heat( txid ):
    txid = hex(txid)
    if len(txid)-2 < 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '90' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('1120', txid))
        print "Translated TXID: ",txid, "\n\n"     
    elif len(txid)-2 >= 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '9' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('1120', txid))
        print "Translated TXID: ",txid, "\n\n"     
    else:
        print("Got a false value!")      
        
        
#Translate the TXID for the FT1 with heat loop to the Final TXID for Risco
def FT1_Heat( txid ):
    txid = hex(txid)
    if len(txid)-2 < 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '90' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('1120', txid))
        print "Translated TXID: ",txid, "\n\n"     
    elif len(txid)-2 >= 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '9' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('1120', txid))
        print "Translated TXID: ",txid, "\n\n"     
    else:
        print("Got a false value!")      



#Translate the TXID for the FT1 with heat loop to the Final TXID for Risco
def HW_SHOCK( txid ):
    txid = hex(txid)
    if len(txid)-2 < 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '30' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('1120', txid))
        print "Translated TXID: ",txid, "\n\n"     
    elif len(txid)-2 >= 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '3' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('1120', txid))
        print "Translated TXID: ",txid, "\n\n"     
    else:
        print("Got a false value!")    

#Error Handler to handle incorrect input
def errhandler():
    print ("Thats incorrect input. Try again: ")

#Translate the TXID for any sensor that involves freeze with heat loop to the Final TXID for Risco
def SMKT3_Freeze( txid ):
    txid = hex(txid)
    if len(txid)-2 < 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '80' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('1120', txid))
        print "Translated TXID: ",txid, "\n\n"     
    elif len(txid)-2 >= 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '8' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('1120', txid))
        print "Translated TXID: ",txid, "\n\n"     
    else:
        print("Got a false value!")       
        
        
#Translate the TXID for any sensor that involves freeze with heat loop to the Final TXID for Risco
def FT1_Freeze( txid ):
    txid = hex(txid)
    if len(txid)-2 < 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '80' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('1120', txid))
        print "Translated TXID: ",txid, "\n\n"     
    elif len(txid)-2 >= 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '8' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('1120', txid))
        print "Translated TXID: ",txid, "\n\n"     
    else:
        print("Got a false value!")   
        
#Translate the TXID for CO3 to the Final TXID for Risco
def CO3( txid ):
    txid = hex(txid)
    if len(txid)-2 < 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '70' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('1120', txid))
        print "Translated TXID: ",txid, "\n\n"     
    elif len(txid)-2 >= 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + '7' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('1120', txid))
        print "Translated TXID: ",txid, "\n\n"     
    else:
        print("Got a false value!")   
        
#Translate the TXID for TILT1 to the Final TXID for Risco
def TILT1( txid ):
    txid = hex(txid)
    if len(txid)-2 < 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + 'C0' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('1120', txid))
        print "Translated TXID: ",txid, "\n\n"     
    elif len(txid)-2 >= 5:
        txid = str(txid)
        index = txid.find('0x')
        txid = txid[:2] + 'C' + txid[2:]
        txid = int(txid, 0)
        txid = str(txid)
        txid = "".join(('112', txid))
        print "Translated TXID: ",txid, "\n\n"     
    else:
        print("Got a false value!")  

#Get the user input
def get_input():
    print("Choose which  sensor you would like to have the TXID translated for:")
    print("--------------------------------------------------------------------")
    print("1. DW10 Magnet ")
    print("2. DW10 External ")
    print("3. SMKT3 ")
    print("4. SMKT3 - Heat ")
    print("5. SMKT3 - Freeze ")
    print("6. GB1-1 ")
    print("7. PIR-1 ")
    print("8. KEY-2, PANIC-1 ")
    print("9. FT-1 ")
    print("10. FT-1 - Heat ")
    print("11. FT-1 - Freeze ")
    print("12. CO3")
    print("13. TILT1")
    print("14. Honeywell Shock Sensors")
    value=int(raw_input("Enter a choice: "))
    
    if value > 14 or value < 1:
        print("Exiting... \n")
        quit()
    else:
        return value

#Main()
def main():
    value = get_input()
    txid = raw_input("Enter the TXID value: ")
    length = len(txid)
    txid = int(txid)
    
    if length == 7:
        takeaction = {
            1: DW10_Magnet,
            2: DW10_External,
            3: SMKT3,
            4: SMKT3_Heat,
            5: SMKT3_Freeze,
            6: GB1,
            7: PIR1,
            8: KEY2_PANIC1,
            9: FT1,
            10: FT1_Heat,
           11: FT1_Freeze,
           12: CO3,
           13: TILT1,
           14: HW_SHOCK,
           }
    
        try:
            takeaction[value] ( txid )
        except KeyError:
            errhandler()
            main()
    else:
        print("You gotta enter 7 digits for the TXID. ")
    main()

#Program start
main()
