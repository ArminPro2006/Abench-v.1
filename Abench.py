from platform import *
# Hello word settings +
print('hello')
# Welcome word settings +
print('welcome to Abench')
# Miane Khat 1 +
print('==================================================')
# Platform import And settings +
processor()
processorG = processor()
# Ps2 +
Ps2 = processorG[0]
Ps2 += processorG[1]
Ps2 += processorG[2]
Ps2 += processorG[3]
Ps2 += processorG[4]
Ps2 += processorG[5]
Ps2 += processorG[6]
# Ps3 +
Ps3 = processorG[0]
Ps3 += processorG[1]
Ps3 += processorG[2]
Ps3 += processorG[3]
Ps3 += processorG[4]
# Setting of Ps2 +
Ps2Bit = ''
if Ps2 == 'Intel64':
    Ps2Bit = 'Your CPU is 64 bit (Intel)'
elif Ps2 == 'Intel32':
    Ps2Bit = 'Your CPU is 32 bit (Intel)'
elif Ps2 == 'Intel86':
    Ps2Bit = 'Your CPU is 32 bit (Intel)'
print(Ps2Bit)
# Setting of Ps3 +
Ps3Bit = ''
if Ps3 == 'AMD64':
    Ps3Bit = 'Your CPU is 64 bit (AMD)'
elif Ps3 == 'AMD86':
    Ps3Bit = 'Your CPU is 32 bit (AMD)'
elif Ps3 == 'AMD32':
    Ps3Bit = 'Your CPU is 32 bit (AMD)'
print(Ps3Bit)
# System Name Settings +
print('Your System name in network is : ' + node())
# platform Settings +
print('Your Windows version is : ' + platform())
# natijeh Settings +
print(architecture())
# Abench Settings +
processorr = processor()
# Intel 64 or 32 or 86 Settings +
processorr1 = processorr[0]
processorr1 += processorr[1]
processorr1 += processorr[2]
processorr1 += processorr[3]
processorr1 += processorr[4]
processorr1 += processorr[5]
processorr1 += processorr[6]
# Family 6 Settings +
processorr2 = processorr[8]
processorr2 += processorr[9]
processorr2 += processorr[10]
processorr2 += processorr[11]
processorr2 += processorr[12]
processorr2 += processorr[13]
processorr2 += processorr[14]
processorr2 += processorr[15]
# model 1 to 165 Settings +
processorr3 = processorr[17]
processorr3 += processorr[18]
processorr3 += processorr[19]
processorr3 += processorr[20]
processorr3 += processorr[21]
processorr3 += processorr[22]
processorr3 += processorr[23]
processorr3 += processorr[24]
processorr3 += processorr[25]
# Miane Khate 2 Settings +
print('==================================================')
# Data Center Settings +
CPUn = ''
CPUdata = ''
if processorr1 == 'Intel64':
    if processorr2 == 'Family 6':
        if processorr3 == 'Model 140':
            CPUn = '37'
            CPUdata = '"Tiger Lake"'
        elif processorr3 == 'Model 126':
            CPUn = '36'
            CPUdata = '"Ice Lake U"'
        elif processorr3 == 'Model 125':
            CPUn = '35'
            CPUdata = '"Ice Lake Y'
        elif processorr3 == 'Model 165':
            CPUn = '34'
            CPUdata = '"Comet Lake S,H"'
        elif processorr3 == 'Model 142':
            CPUn = '33'
            CPUdata = '"Comet Lake U" or "Amber Lake Y" or "Whiskey Lake U"'
        elif processorr3 == 'Model 102':
            CPUn = '32'
            CPUdata = '"Cannon Lake U"'
        elif processorr3 == 'Model 158':
            CPUn = '31'
            CPUdata = '"Coffee Lake S,H,E"'
        elif processorr3 == 'Model 142':
            CPUn = '30'
            CPUdata = '"Coffee Lake U"'
        elif processorr3 == 'Model 158':
            CPUn = '29'
            CPUdata = '"Kaby Lake DT,H,S,X"'
        elif processorr3 == 'Model 142':
            CPUn = '28'
            CPUdata = '"Kaby Lake U,Y"'
        elif processorr3 == 'Model 94 ':
            CPUn = '27'
            CPUdata = '"Skylake DT,H,S"'
        elif processorr3 == 'Model 78 ':
            CPUn = '26'
            CPUdata = '"Skylake U,Y"'
        elif processorr3 == 'Model 71 ':
            CPUn = '25'
            CPUdata = '"Broadwell C,W,H"'
        elif processorr3 == 'Model 61 ':
            CPUn = '24'
            CPUdata = '"Broadwell U,Y,S"'
        elif processorr3 == 'Model 70 ':
            CPUn = '23'
            CPUdata = '"Haswell GT3E"'
        elif processorr3 == 'Model 69 ':
            CPUn = '22'
            CPUdata = '"Haswell ULT"'
        elif processorr3 == 'Model 60 ':
            CPUn = '21'
            CPUdata = '"Haswell S"'
        elif processorr3 == 'Model 58 ':
            CPUn = '20'
            CPUdata = '"Ivy Bridge M,H,Gladden"'
        elif processorr3 == 'Model 42 ':
            CPUn = '19'
            CPUdata = '"Sandy Bridge M,H"'
        elif processorr3 == 'Model 37 ':
            CPUn = '18'
            CPUdata = '"Westmere Arrandale,Clarkdale"'
        elif processorr3 == 'Model 31 ':
            CPUn = '17'
            CPUdata = '"Nehalem"'
        elif processorr3 == 'Model 30 ':
            CPUn = '16'
            CPUdata = '"Nehalem Clarksfield"'
        elif processorr3 == 'Model 23 ':
            CPUn = '15'
            CPUdata = '"Penryn Penryn, Wolfdale, Yorkfield"'
        elif processorr3 == 'Model 22 ':
            CPUn = '14'
            CPUdata = '"Core Merom L"'
        elif processorr3 == 'Model 15 ':
            CPUn = '13'
            CPUdata = '"Core Merom"'
        elif processorr3 == 'Model 14 ':
            CPUn = '12'
            CPUdata = '"Modified Pentium M"'
        elif processorr3 == 'Model 21 ':
            CPUn = '11'
            CPUdata = '"Pentium M Tolapai"'
        elif processorr3 == 'Model 13 ':
            CPUn = '10'
            CPUdata = '"Pentium M Dothan"'
        elif processorr3 == 'Model 9 S':
            CPUn = '9'
            CPUdata = '"Pentium M Banias"'
        elif processorr3 == 'Model 11 ':
            CPUn = '8'
            CPUdata = '"P6 Tualatin"'
        elif processorr3 == 'Model 8 S':
            CPUn = '7'
            CPUdata = '"P6 Coppermine, Coppermine T"'
        elif processorr3 == 'Model 7 S':
            CPUn = '6'
            CPUdata = '"P6 Katmai"'
        elif processorr3 == 'Model 6 S':
            CPUn = '5'
            CPUdata = '"P6"'
        elif processorr3 == 'Model 5 S':
            CPUn = '4'
            CPUdata = '"P6"'
        elif processorr3 == 'Model 3 S':
            CPUn = '3'
            CPUdata = '"P6"'
        elif processorr3 == 'Model 2 S':
            CPUn = '2'
            CPUdata = '"P6"'
        elif processorr3 == 'Model 1 S':
            CPUn = '1'
            CPUdata = '"P6"'
        else:
            CPUdata = 'The processor is not defined in the data center !'
print('Your CPU Model is : ' + CPUdata)
# CPU ID Settings +
CPULevel = ""
if CPUdata == '"Tiger Lake"':
    CPULevel = 'Your CPU good for : Gaming , Editing , Graphic works'
elif CPUdata == '"Ice Lake U"':
    CPULevel = 'Your CPU good for : Gaming , Editing / and bad for : Graphic works'
elif CPUdata == '"Ice Lake Y"':
    CPULevel = 'Your CPU good for : Editing / and bad for : Gaming , Graphic works'
elif CPUdata == '"Comet Lake S,H"':
    CPULevel = 'Your CPU good for : Editing , Gaming , Graphic works'
elif CPUdata == '"Comet Lake U" or "Amber Lake Y" or "Whiskey Lake U"':
    CPULevel = 'Your CPU good for : Editing , Gaming / and bad for : Graphic works'
elif CPUdata == '"Cannon Lake U"':
    CPULevel = 'Your CPU good for : Editing , Gaming / and bad for : Graphic works'
elif CPUdata == '"Coffee Lake S,H,E"':
    CPULevel = 'Your CPU good for : Editing , Gaming , Graphic works'
elif CPUdata == '"Coffee Lake U"':
    CPULevel = 'Your CPU good for : Editing , Gaming / and bad for : Graphic works'
elif CPUdata == '"Kaby Lake DT,H,S,X"':
    CPULevel = 'Your CPU good for : Editing , Gaming , Graphic works'
elif CPUdata == '"Kaby Lake U,Y"':
    CPULevel = 'Your CPU good for : Editing / and bad for : Gaming , Graphic works'
elif CPUdata == '"Skylake DT,H,S"':
    CPULevel = 'Your CPU good for : Editing , Gaming , Graphic works'
elif CPUdata == '"Skylake U,Y"':
    CPULevel = 'Your CPU good for : Editing / and bad for : Gaming , Graphic works'
elif CPUdata == '"Broadwell C,W,H"':
    CPULevel = 'Your CPU good for : Editing , Gaming / and bad for : Graphic works'
elif CPUdata == '"Broadwell U,Y,S"':
    CPULevel = 'Your CPU good for : Editing / and bad for : Graphic works , Gaming'
elif CPUdata == '"Haswell ULT"':
    CPULevel = 'Your CPU good for : Editing / and bad for : Graphic works , Gaming'
elif CPUdata == '"Haswell S"':
    CPULevel = 'Your CPU good for : Editing , Gaming / and bad for : Graphic works'
elif CPUdata == '"Ivy Bridge M,H,Gladden"':
    CPULevel = 'Your CPU good for : Editing / and bad for : Graphic works , Gaming'
elif CPUdata == '"Sandy Bridge M,H"':
    CPULevel = 'Your CPU good for : Editing / and bad for : Graphic works , Gaming'
elif CPUdata == '"Westmere Arrandale,Clarkdale"':
    CPULevel = 'Your CPU good for : Editing / and bad for : Graphic works , Gaming'
elif CPUdata == '"Nehalem"':
    CPULevel = 'Your CPU good for : Editing / and bad for : Graphic works , Gaming'
elif CPUdata == '"Nehalem Clarksfield"':
    CPULevel = 'Your CPU good for : Editing / and bad for : Graphic works , Gaming'
elif CPUdata == '"Penryn Penryn, Wolfdale, Yorkfield"':
    CPULevel = 'Your CPU is bad'
elif CPUdata == '"Core Merom L"':
    CPULevel = 'Your CPU is bad'
elif CPUdata == '"Core Merom"':
    CPULevel = 'Your CPU is bad'
elif CPUdata == '"Modified Pentium M"':
    CPULevel = 'Your CPU is bad'
elif CPUdata == '"Pentium M Tolapai"':
    CPULevel = 'Your CPU is bad'
elif CPUdata == '"Pentium M Dothan"':
    CPULevel = 'Your CPU is bad'
elif CPUdata == '"Pentium M Banias"':
    CPULevel = 'Your CPU is bad'
elif CPUdata == '"P6 Tualatin"':
    CPULevel = 'Your CPU is bad'
elif CPUdata == '"P6 Coppermine, Coppermine T"':
    CPULevel = 'Your CPU is bad'
elif CPUdata == '"P6"':
    CPULevel = 'Your CPU is bad'
print(CPULevel)
# Miane Khate 3 Settings +
print('==================================================')
# made by Settings +
print('Made by Armin Rahimi (A.R.i)')
# Miane Khate 4 Settings +
print('==================================================')
# input Gamer or Editer
#Clear commandline
from subprocess import call
from sys import platform
def clear():
    if platform not in ('win32', 'cygwin'):
        command = 'clear'
    else:
        command = 'cls'
    try:
        call(command, shell=True)
    except OSError as e:
        print(type(e).__name__, e)
print('''
         11100101101010110010110111    11100101101010110010110111
         11100101101010110010110111    11100101101010110010110111
         11100101101010110010110111    11100101101010110010110111
         11100101101010110010110111    11100101101010110010110111
         11100101101010110010110111    11100101101010110010110111
         11100101101010110010110111    11100101101010110010110111
                                                
         11100101101010110010110111    11100101101010110010110111
         11100101101010110010110111    11100101101010110010110111
         11100101101010110010110111    11100101101010110010110111
         11100101101010110010110111    11100101101010110010110111
         11100101101010110010110111    11100101101010110010110111
         11100101101010110010110111    11100101101010110010110111''')
GGE = input(
    'Enter the name of the software or game you want to compare and press Enter : ').lower()
# Data center of Games +
# FiFa Gamme
CPUpn = ''
fifa9 = '9'
if GGE == 'fifa9':
    if CPUn >= '10':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    fifa10 = '10'
elif GGE == 'fifa10':
    if CPUn >= '10':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    fifa11 = '12'
elif GGE == 'fifa11':
    if CPUn >= '12':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    fifa12 = '13'
elif GGE == 'fifa12':
    if CPUn >= '13':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    fifa13 = '13'
elif GGE == 'fifa13':
    if CPUn >= '14':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    fifa14 = '14'
elif GGE == 'fifa14':
    if CPUn >= '14':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    fifa15 = '15'
elif GGE == 'fifa15':
    if CPUn >= '15':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    fifa16 = '16'
elif GGE == 'fifa16':
    if CPUn >= '15':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    fifa17 = '17'
elif GGE == 'fifa17':
    if CPUn >= '17':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    fifa18 = '18'
elif GGE == 'fifa18':
    if CPUn >= '18':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    fifa19 = '19'
elif GGE == 'fifa19':
    if CPUn >= '19':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    fifa20 = '20'
elif GGE == 'fifa20':
    if CPUn >= '20':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    fifa21 = '21'
elif GGE == 'fifa21':
    if CPUn >= '26':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
# PES Game
    pes2009 = '9'
elif GGE == 'pes2009':
    if CPUn >= '10':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    pes2010 = '10'
elif GGE == 'pes2010':
    if CPUn >= '10':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    pes2011 = '11'
elif GGE == 'pes2011':
    if CPUn >= '11':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    pes2012 = '12'
elif GGE == 'pes2012':
    if CPUn >= '11':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    pes2013 = '13'
elif GGE == 'pes2013':
    if CPUn >= '11':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    pes2014 = '14'
elif GGE == 'pes2014':
    if CPUn >= '11':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    pes2015 = '15'
elif GGE == 'pes2015':
    if CPUn >= '14':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    pes2016 = '16'
elif GGE == 'pes2016':
    if CPUn >= '14':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    pes2017 = '17'
elif GGE == 'pes2017':
    if CPUn >= '14':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    pes2018 = '18'
elif GGE == 'pes2018':
    if CPUn >= '19':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    pes2019 = '19'
elif GGE == 'pes2019':
    if CPUn >= '19':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    pes2020 = '20'
elif GGE == 'pes2020':
    if CPUn >= '19':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    pes2021 = '21'
elif GGE == 'pes2021':
    if CPUn >= '20':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
# NFS
    NFS_underground = '1'
elif GGE == 'nfsunderground':
    if CPUn >= '10':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    NFS_underground2 = '1'
elif GGE == 'nfsunderground2':
    if CPUn >= '10':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    NFS_mostwanted = '3'
elif GGE == 'nfsmostwanted':
    if CPUn >= '10':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    NFS_carbon = '4'
elif GGE == 'nfscarbon':
    if CPUn >= '10':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    NFS_prostreet = '5'
elif GGE == 'nfsprostreet':
    if CPUn >= '11':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    NFS_undercover = '6'
elif GGE == 'nfsundercover':
    if CPUn >= '12':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    NFS_shift = '7'
elif GGE == 'nfsundercover':
    if CPUn >= '13':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    NFS_hotpursuit = '8'
elif GGE == 'nfshotpursuit':
    if CPUn >= '13':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    NFS_therun = '9'
elif GGE == 'nfstherun':
    if CPUn >= '14':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    NFS_mostwanted2 = '10'
elif GGE == 'nfsmostwanted2':
    if CPUn >= '14':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    NFS_rivals = '11'
elif GGE == 'nfsrivals':
    if CPUn >= '15':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    NFS_needforspeed = '12'
elif GGE == 'nfsneedforspeed':
    if CPUn >= '20':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    NFS_payback = '13'
elif GGE == 'nfspayback':
    if CPUn >= '26':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    NFS_heat = '14'
elif GGE == 'nfsheat':
    if CPUn >= '26':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
# Cal of duty
    Call_of_Duty1 = '10'
elif GGE == 'cod1':
    if CPUn >= '10':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    Call_of_Duty2 = '10'
elif GGE == 'cod2':
    if CPUn >= '10':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    Call_of_Duty3 = '10'
elif GGE == 'cod3':
    if CPUn >= '10':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    Call_of_Duty4 = '10'
elif GGE == 'cod4':
    if CPUn >= '10':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    Call_of_Duty5 = '11'
elif GGE == 'cod5':
    if CPUn >= '11':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    Call_of_Duty6 = '12'
elif GGE == 'cod6':
    if CPUn >= '12':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    Call_of_Duty7 = '14'
elif GGE == 'cod7':
    if CPUn >= '14':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    Call_of_Duty8 = '14'
elif GGE == 'cod8':
    if CPUn >= '14':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    Call_of_Duty9 = '14'
elif GGE == 'cod9':
    if CPUn >= '14':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    Call_of_Duty10 = '14'
elif GGE == 'cod10':
    if CPUn >= '14':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    Call_of_Duty11 = '15'
elif GGE == 'cod11':
    if CPUn >= '15':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    Call_of_Duty12 = '16'
elif GGE == 'cod12':
    if CPUn >= '16':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    Call_of_Duty13 = '19'
elif GGE == 'cod13':
    if CPUn >= '19':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    Call_of_Duty14 = '19'
elif GGE == 'cod14':
    if CPUn >= '19':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    Call_of_Duty15 = '21'
elif GGE == 'cod15':
    if CPUn >= '19':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    Call_of_Duty16 = '21'
elif GGE == 'cod16':
    if CPUn >= '21':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
    Call_of_Duty17 = '26'
elif GGE == 'cod17':
    if CPUn >= '26':
        CPUpn = 'You can run this game!'
    else:
        CPUpn = 'You can not run this game!'
# Data center of Edit N +
    Photoshop = 'photoshop'
elif GGE == 'photoshop':
    if CPUn >= '15':
        CPUpn = 'You can run this app!'
    else:
        CPUpn = 'You can not run this app!'
    Adobe_Peremiere_Pro = '15'
elif GGE == 'peremiere':
    if CPUn >= '15':
        CPUpn = 'You can run this app!'
    else:
        CPUpn = 'You can not run this app!'
    Adobe_After_Effects = '15'
elif GGE == 'aftereffects':
    if CPUn >= '15':
        CPUpn = 'You can run this app!'
    else:
        CPUpn = 'You can not run this app!'
    Filmora = '8'
elif GGE == 'filmora':
    if CPUn >= '10':
        CPUpn = 'You can run this app!'
    else:
        CPUpn = 'You can not run this app!'
    Davinci_Resolve = '126'
elif GGE == 'davinci':
    if CPUn >= '36':
        CPUpn = 'You can run this app!'
    else:
        CPUpn = 'You can not run this app!'
    Windows_Movie_Maker = '10'
elif GGE == 'windowsmovie':
    if CPUn >= '10':
        CPUpn = 'You can run this app!'
    else:
        CPUpn = 'You can not run this app!'
    Blender = '12'
elif GGE == 'belender':
    if CPUn >= '12':
        CPUpn = 'You can run this app!'
    else:
        CPUpn = 'You can not run this app!'
    Lightworks = '10'
elif GGE == 'lghtworks':
    if CPUn >= '10':
        CPUpn = 'You can run this app!'
    else:
        CPUpn = 'You can not run this app!'
    VideoPad = '10'
elif GGE == 'videopad':
    if CPUn >= '10':
        CPUpn = 'You can run this app!'
    else:
        CPUpn = 'You can not run this app!'
    Illustrator = '16'
elif GGE == 'illustrator':
    if CPUn >= '16':
        CPUpn = 'You can run this app!'
    else:
        CPUpn = 'You can not run this app!'
    CorelDraw = '16'
elif GGE == 'corel':
    if CPUn >= '16':
        CPUpn = 'You can run this app!'
    else:
        CPUpn = 'You can not run this app!'
    InDesign = '16'
elif GGE == 'indesing':
    if CPUn >= '16':
        CPUpn = 'You can run this app!'
    else:
        CPUpn = 'You can not run this app!'
    D3_Max = '36'
elif GGE == '3dmax':
    if CPUn >= '21':
        CPUpn = 'You can run this app!'
    else:
        CPUpn = 'You can not run this app!'
    Maya = '36'
elif GGE == 'maya':
    if CPUn >= '21':
        CPUpn = 'You can run this app!'
    else:
        CPUpn = 'You can not run this app!'
    Lightroom = '16'
elif GGE == 'lightroom':
    if CPUn >= '16':
        CPUpn = 'You can run this app!'
    else:
        CPUpn = 'You can not run this app!'
    Gimp = '16'
elif GGE == 'gimp':
    if CPUn >= '16':
        CPUpn = 'You can run this app!'
    else:
        CPUpn = 'You can not run this app!'
    InkScape = '10'
elif GGE == 'inkscape':
    if CPUn >= '10':
        CPUpn = 'You can run this app!'
    else:
        CPUpn = 'You can not run this app!'
else:
    CPUpn = 'Not available in the database!'
# Data center of Games 2 +
print(CPUpn)
quit = input('press Enter key to exit !')