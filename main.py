import streamlit as st
import pandas as pd
import bz2
import pathlib
import pickle as cPickle
import pvlib

st.title('Modules and inverters _PVLib_ database for _EMHASS_')

root = pathlib.Path(__file__).parent.resolve()
cec_modules = bz2.BZ2File(str(root / pathlib.Path('data/cec_modules.pbz2')), "rb")
cec_modules = cPickle.load(cec_modules)
cec_inverters = bz2.BZ2File(str(root / pathlib.Path('data/cec_inverters.pbz2')), "rb")
cec_inverters = cPickle.load(cec_inverters)

df_modules_result_search = pd.DataFrame()
df_inverters_result_search = pd.DataFrame()

st.header('PV Modules', divider='blue')
# module_name_search = 'CSUN295'
module_name_search = st.text_input("Module name (Partial name, not case sensitive, Ex: CSUN295)")
df_modules_result_search = cec_modules.loc[:,cec_modules.columns.str.contains(module_name_search, case=False, na=False)]
num_modules = df_modules_result_search.shape[1]
st.write("{} Records found for PV modules".format(str(num_modules)))
if num_modules >= 100:
    st.write("Writing only when records found is < 100, try changing your search name")
else:
    st.dataframe(df_modules_result_search)

st.header('PV Inverters', divider='blue')
# inverter_name_search = 'Fronius_Primo'
inverter_name_search = st.text_input("Inverter name (Partial name, not case sensitive, Ex: Fronius_Primo)")
df_inverters_result_search = cec_inverters.loc[:,cec_inverters.columns.str.contains(inverter_name_search, case=False, na=False)]
num_inverters = df_inverters_result_search.shape[1]
st.write("{} Records found for PV inverters".format(str(num_inverters)))
if num_inverters >= 100:
    st.write("Writing only when records found is < 100, try changing your search name")
else:
    st.dataframe(df_inverters_result_search)
