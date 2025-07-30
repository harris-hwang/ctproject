import streamlit as st
import streamlit.components.v1 as htmlviewer
# Title Msg#1
st.title('This is HWANG!')

with open('./index1.html', 'r', encoding='utf-8') as f:
    html1 = f.read()
    f.close()
with open('./index2.html', 'r', encoding='utf-8') as f:
    html2 = f.read()
    f.close()
with open('./index3.html', 'r', encoding='utf-8') as f:
    html3 = f.read()
    f.close()

# html = '''
# <html>
#     <head>
#         <title> this is my html </title>
#     </head>
#     <body>
#         <h1>Topic</h1>
#         <h2>SubTopic</h2>
#     </body>
# </html>
# '''
# Box#1(4), Box#2(1)
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('식물 잎의 개수 구하기'):
        #st.write(html1, unsafe_allow_html=True)
        htmlviewer.html(html1,height=600)
    with st.expander('역학적 에너지 보존'):
        #st.write(html2, unsafe_allow_html=True)
        htmlviewer.html(html2,height=600)
    with st.expander('빛의 3원색을 이용한 빛의 색 찾기'):
        #st.write(html3, unsafe_allow_html=True)
        htmlviewer.html(html3,height=600)
with col2:
    with st.expander('Tips..'):
        st.info('Tips..')
st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by Hwang', unsafe_allow_html=True)