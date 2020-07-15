import streamlit as st
import warnings
import pandas as pd
from venn import venn
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

STYLE = """
<style>
img {
    max-width: 100%;
}
</style>
"""

def draw_for_two(csv_file,select_cols):
	data = csv_file[select_cols]
	set1 = set(data[select_cols[0]])
	set2 = set(data[select_cols[1]])
	set1 = {x for x in set1 if pd.notna(x)}
	set2 = {x for x in set2 if pd.notna(x)}
	data_dict = {}
	data_dict['s1'] = set1
	data_dict['s2'] = set2
	venn(data_dict)
	st.pyplot()

def draw_for_three(csv_file, select_cols):
	data = csv_file[select_cols]
	set1 = set(data[select_cols[0]])
	set2 = set(data[select_cols[1]])
	set3 = set(data[select_cols[2]])
	set1 = {x for x in set1 if pd.notna(x)}
	set2 = {x for x in set2 if pd.notna(x)}
	set3 = {x for x in set3 if pd.notna(x)}
	data_dict = {}
	data_dict['s1'] = set1
	data_dict['s2'] = set2
	data_dict['s3'] = set3
	venn(data_dict)
	st.pyplot()

def draw_for_four(csv_file, select_cols):
	data = csv_file[select_cols]
	set1 = set(data[select_cols[0]])
	set2 = set(data[select_cols[1]])
	set3 = set(data[select_cols[2]])
	set4 = set(data[select_cols[3]])
	set1 = {x for x in set1 if pd.notna(x)}
	set2 = {x for x in set2 if pd.notna(x)}
	set3 = {x for x in set3 if pd.notna(x)}
	set4 = {x for x in set4 if pd.notna(x)}
	data_dict = {}
	data_dict['s1'] = set1
	data_dict['s2'] = set2
	data_dict['s3'] = set3
	data_dict['s4'] = set4
	venn(data_dict)
	st.pyplot()

def draw_for_five(csv_file, select_cols):
	data = csv_file[select_cols]
	set1 = set(data[select_cols[0]])
	set2 = set(data[select_cols[1]])
	set3 = set(data[select_cols[2]])
	set4 = set(data[select_cols[3]])
	set5 = set(data[select_cols[4]])
	set1 = {x for x in set1 if pd.notna(x)}
	set2 = {x for x in set2 if pd.notna(x)}
	set3 = {x for x in set3 if pd.notna(x)}
	set4 = {x for x in set4 if pd.notna(x)}
	set5 = {x for x in set5 if pd.notna(x)}
	data_dict = {}
	data_dict['s1'] = set1
	data_dict['s2'] = set2
	data_dict['s3'] = set3
	data_dict['s4'] = set4
	data_dict['s5'] = set5
	venn(data_dict)
	st.pyplot()

FILE_TYPES = ['csv']

st.title('Venn Diagram App')
st.subheader('build with Streamlit')
st.write('To download Image (right-click on image and select save image as)')

file = st.file_uploader('Upload file', type=FILE_TYPES)
show_file = st.empty()
if not file:
    show_file.info('Please upload a file of type: '+','.join(FILE_TYPES))

csv_file = pd.read_csv(file)
select_cols = st.multiselect('Select columns',list(csv_file.columns))

opt = st.radio('Select option',('Draw for 2 sets', 'Draw for 3 sets', 'Draw for 4 sets', 'Draw for 5 sets'))

if opt == 'Draw for 2 sets':
	draw_for_two(csv_file,select_cols)

if opt == 'Draw for 3 sets':
	draw_for_three(csv_file, select_cols)

if opt == 'Draw for 4 sets':
	draw_for_four(csv_file, select_cols)

if opt == 'Draw for 5 sets':
	draw_for_five(csv_file, select_cols)