from django.http.response import HttpResponse
from django.shortcuts import render
import africastalking
from django.views.decorators.csrf import csrf_exempt
from .models import *
#  python3 -m pip install africastalking
AfricasUsername='rukundojamie@gmail.com'
api_key ='0e2088e0e7563fe5fd0cc9007cd3e9061a326a1647fecaa45d2f81b518ac35dc'
africastalking.initialize(AfricasUsername,api_key)

@csrf_exempt
def ussdApp(request):

    if request.method == 'POST':
        session_id = request.POST.get("sessionId")
        service_code = request.POST.get("serviceCode")
        phone_number =request.POST.get("phoneNumber")
        text = request.POST['text']
        level = text.split('*')
        category = text[:3]
        response =""

        #  our application menu

        if text == '':
            response =  "CON Ikaze kuri chiafarm \n"
            response += "1. Kugura igihingwa cya chia \n"
            response += "2. Amakuru y'ibanze y'igihingwa cya chia seeds ukwiye "
            response += " gusoma mbere yo kugura iki gihingwa"


        elif text == '1':
            response = "CON Hitamo ubwoko bw'igihingwa \n"
            response += "1. Imbuto za chia z'umweru \n"
            response += "2. Imbuto za chia z'umukara"


        elif text == '1*1':
            product="imbuto za chia z'umweru "
            response = "CON shyiramo ingano y'"+str(product)+" ushaka mu biro \n"


        elif category =='1*1' and int(len(level)) == 3 and str(level[2]) in  str(level):
            response = "CON Shyiramo amafaranga \n"

        elif category =='1*1' and int(len(level)) == 4 and str(level[3]) in  str(level):
            if int(level[3]) != int(level[2]) * int(3000):
                response = "CON Washyizemo amafaranga make \n"
            else:
                response = "END Murakoze kugura imbuto za chia kuri chiafarm!  \n"


        elif text == '1*2':
            product ="imbuto za chia z'umukara"
            response ="CON shyiramo ingano y'"+str(product)+" ushaka mu biro \n"


        elif category =='1*2' and int(len(level)) == 3 and str(level[2]) in  str(level):
            response = "CON Shyiramo amafaranga  \n"

        elif category =='1*2' and int(len(level)) == 4 and str(level[3]) in  str(level):
            response = "END Murakoze kugura imbuto za chia kuri chiafarm! \n"
         
        #  ======================== AMAKURU Y'IGIHINGWA CYA CHIA SEED ==================

        elif text == '2':
            response = "CON Igihingwa cya chia seed ni imbuto zifite ibara ry'umweru cq ry'umukara zikomoka"
            response += "muri Amarica y'amajyepfo ho muri Mexico na Quatemara. Urubuto rumwe rwa chia seed"
            response += "rupima umurambararo wa milimetero imwe (1). Ni ubwoko bw'imbuto z'ibinyampeke."
            response += "Zishobora kuribwa uko zakabaye zivanywe mu murima, zishobora gusebwamo "
            response += "ifu cyangwa se zigakorwamo amavuta yaba ayo kurya cyangwa se ayo kwisiga."
            response += "Izi mbuto iyo uzishyize mu mazi, rumwe rukurura amazi akubye incuro 12 uburemere "
            response += "bwarwo, maze rukabyimba. izi mbuto ni igihingwa kerera amezi atatu gusa kandi ikiro kimwe"
            response += "cyazo kigura nibura amafaranga y'u Rwanda 3000. ni ukuvuga ko ikiro kimwe cya "
            response += "chia seed kinganya agaciro mu mafaranga n'ibiro 15 by'ikawa y'ibitumbwe yereye"
            response += "amezi 12, kingana n'ibiro 20 by'ibijumba, kingana n'ibiro 5 by'ibishyimbo uramutse"
            response += "ubaze ku mafaranga 400 kuri buri kiro. ikiro cya chia seed kinganya amafaranga n'ibiro"
            response += "3 by'umuceri cyangwa se ibiro 7 by'ubugari. ibiro 2 by'izi mbuto bitera hegitari "
            response += "y'ubutaka maze mu mezi atatu zikaba zeze ibiro igihumbi! Ikindi kiza kurusha ni uko"
            response += "igihingwa cya chia seed gihingwa hadakoreshejwe ifumbire mva ruganda cyangwa se imiti"
            response += "yica udukoko. Uburyo zihingwa, barazitera bagashyiramo ifumbire y'imborera bakazuhira "
            response += "bihagije ubundi zikera. Mu Rwanda izi mbuto zahageze mu mwaka wa 2017."
        
        return HttpResponse(response)