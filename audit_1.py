import pandas as pd
onex=pd.read_excel(r'\Users\ASUS\Desktop\PythonFiles\hand.xlsx')
#onex.columns
#onex['a']
item_card=[i.upper() for i in onex['b'].values.tolist()[10:7902:1]];
item_name=[i.upper() for i in onex['a.1'].values.tolist()[10:7902:1]];
item_slip=onex['b.1'].values.tolist()[10:7902:1];
item_ledger=onex['a.4'].values.tolist()[10:7902:1];
item_unit_cost=onex['b.8'].values.tolist()[10:7902:1];
item_cost=onex['a.9'].values.tolist()[10:7902:1];

onex1=pd.read_excel(r'\Users\ASUS\Desktop\PythonFiles\online.xlsx')
item1_card=[i.upper() for i in onex1['Unnamed: 2'].values.tolist()[15:7774:1]];
item1_name=[];item1_code=[];
item2_name=onex1['Unnamed: 6'].values.tolist()[15:7774:1];
for i in item2_name:
    item1_name.append(i.split(" (Code ")[0]);
    item1_code.append(i.split(" (Code ")[1]);
item1_slip=onex1['Unnamed: 7'].values.tolist()[15:7774:1];
item1_page=onex1['Unnamed: 9'].values.tolist()[15:7774:1];
item1_ledger=onex1['Unnamed: 13'].values.tolist()[15:7774:1];
item1_unit_cost=onex1['Unnamed: 33'].values.tolist()[15:7774:1];
item1_cost=onex1['Unnamed: 35'].values.tolist()[15:7774:1];
found=[];
for j in range(0,len(item_name)):
    hand_name=item_name[j];
    h1=set();h2=set();h3=set();h4=set();
    for k in range(0,len(item1_name)):
        on_name=item1_name[k];
        [h1.add(f) for f in hand_name];
        [h2.add(f) for f in on_name];
        [h3.add(f) for f in item_card[j]];
        [h4.add(f) for f in item1_card[k]];
        if hand_name[0]==on_name[0] and len(hand_name)>=len(on_name) and (len(h1)-len(h2)>1 or len(h1)-len(h2)<1) and (len(h3)-len(h4)>1 or len(h3)-len(h4)<1):
            if (item_cost[j]-item1_cost[k]<20 or item_cost[j]-item1_cost[k]>20) and item_card[k]==item1_card[j] :
                break
            else:
                found.append(on_name)
                

            
