#!/usr/bin/env python
# coding: utf-8

# In[90]:


from FetchPrice import *
from EVEBlueprints import *
from EVEIndustrier import do_get_input_info_rtn
from EVEIndustry_v2 import get_inputs_rtn
from NamesTranslator import get_type_name


# In[91]:


def get_production_chain(bp_id):
    inputs = get_inputs_rtn(bp_id)
    result = []
    for k,v in inputs.items():
        try:
            i_bp = get_blueprint_from_product(k)
            result.append(get_type_name(i_bp))
            result.append(get_production_chain(i_bp))
        except IndexError:
            result.append({k: v})
    return result


# In[92]:


def print_format_chain(chain, iter=0):
    for i in chain:
        if type(i) == type([]):
            print_format_chain(i, iter + 1)
        elif type(i) == type({}):
            print(" " * 2 * iter + "`---" + get_type_name(list(i.keys())[0]) + " x" + str(list(i.values())[0]))
        elif type(i) == type(""):
            print(" " * 2 * iter + "`-" + i)


# In[140]:





# In[142]:


id = 11380

chain = get_production_chain(id)

print("==========%s==========" %get_type_name(id))
#print("Production Cost:" + str(calc_price(chain)))
print("")
print("Inputs")
print_format_chain(chain)

input()

# In[ ]:




