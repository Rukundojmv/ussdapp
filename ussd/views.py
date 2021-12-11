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
            response += "2. Iby'ibanze ukwiye kumenya ku gihingwa "
            response += " cya chia seeds mbere y'uko ukigura"


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
                response = "END Washyizemo amafaranga atajyanye n'ibiro by'imbuto ushaka \n"
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
            response = "Hitamo amakuru y'igihingwa \n"
            response += "1. Amakuru y'ibanze \n"
            response += "2. Uko imbuto za chia zihingwa \n"
            response += "3. Imikoreshereze y'imbuto za chia n'agaciro kazo \n"
            response += "4. Intungamubiri ziboneka mu mbuto za chia \n"


        # elif text == '2*1':
        #     response = "CON Igihingwa cya chia seed ni imbuto zifite ibara ry'umweru cq ry'umukara zikomoka"
        #     response += "muri Amarica y'amajyepfo ho muri Mexico na Quatemara. Urubuto rumwe rwa chia seed"
        #     response += "rupima umurambararo wa milimetero imwe (1). Ni ubwoko bw'imbuto z'ibinyampeke."
        #     response += "Izi mbuto iyo uzishyize mu mazi, rumwe rukurura amazi akubye incuro 12 uburemere "
        #     response += "bwarwo, maze rukabyimba. Izi mbuto ni igihingwa kerera amezi atatu gusa kandi "
        #     response += "ikiro kimwe cyazo kigura nibura amafaranga y'u Rwanda 3000."
        #     response += "Izi mbuto zikaba zarageze mu Rwanda mu mwaka wa 2017."


        # elif text == '2*2':
        #     response = "CON ibiro 2 by'izi mbuto bitera hegitari y'ubutaka maze mu mezi atatu zikaba "
        #     response += "zeze ibiro igihumbi! Ikindi kiza kurushaho ni uko igihingwa cya chia seed "
        #     response += "gihingwa hadakoreshejwe ifumbire mva ruganda cyangwa se imiti yica udukoko."
        #     response += "Uburyo zihingwa, barazitera bagashyiramo ifumbire y'imborera bakazuhira "
        #     response += "bihagije ubundi zikera."


        # elif text == '2*3':
        #     response = "CON Imbuto za chia seeds zishobora kuribwa uko zakabaye zivanywe mu murima, "
        #     response += "zishobora gusebwamo ifu cyangwa se zigakorwamo amavuta yaba ayo kurya"
        #     response += " cyangwa se ayo kwisiga. Mu gaciro, ikiro kimwe cy'igihingwa cya chia seeds "
        #     response += "kinganya agaciro mu mafaranga n'ibiro 15 by'ikawa y'ibitumbwe yereye amezi 12, "
        #     response += " kingana n'ibiro 20 by'ibijumba, kingana n'ibiro 5 by'ibishyimbo uramutse ubaze "
        #     response += "ku mafaranga 400 kuri buri kiro. ikiro cya chia seeds kandi kinganya amafaranga "
        #     response += "n'ibiro 3 by'umuceri cyangwa se ibiro 7 by'ubugari."
        return HttpResponse(response)