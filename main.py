from azure.core.credentials import AzureKeyCredential   #only credential
from azure.ai.formrecognizer import FormRecognizerClient #custom Model ke liye hai

endpoint = "https://iris-metadata-extraction.cognitiveservices.azure.com/"
key = "de872f4a158b47e8957c06ed3b9fccea"
model_id = "e003721b-6523-4e94-8178-04d5487629a5"

form_recognizer_client = FormRecognizerClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

# Make sure your form's type is included in the list of form types the custom model can recognize
filename=r'C:\Users\V4SWHVY\Downloads\τkoda auto - 08_22 autovraky dopln╪ní.pdf'
with open(filename, "rb") as f:
    poller = form_recognizer_client.begin_recognize_custom_forms(
        model_id=model_id, form=f
    )
forms = poller.result()

wasteN =""
partnerId =""
for form in forms:
    print("{")
    for name, field in form.fields.items():
        #hw --> structure se json!!
        
        if name != 'LineItem':
            print(name,": ",field.value)

            if name=='wasteName':
                wasteN = field.value
            if name=='partnerIdentifier':
               partnerId = field.value 
            # wasteN = field.value if name=='wasteName' else ""
            # partnerId = field.value if name=='partnerIdentifier' else ""
            # print("partID",partnerId)
        else:
            print(name,": ","{")
            for txt in field.value:
                # print(txt.value)
                print("\t{\n")
                for data in txt.value.values():  #txt.value gives names
                    data_name=data.name
                    if(data_name == 'partnerIdentifier'):
                        data_value=partnerId
                    elif(data_name == 'wasteName'):
                        data_value=wasteN
                    else:
                        data_value = data.value
                    # data_value=partnerId if data.value=='None' and data.name==partnerIdentifier else data.value
                    # data_value=wasteN if data.value=='None' and data.name==wasteName else data.value

                    print("\t",data_name,":",data_value,"\n")
                print("\t}\n")
            print("    }")
    print("}")

        
            # print("...Field '{}' has label '{}' with a confidence score of {}".format(
            #     name,
            #     field.label_data.text,
            #     field.confidence
            # ))

        

   