import streamlit as st
import streamlit.components.v1 as htmlviewer

# Custom CSS for larger text elements
st.markdown("""
<style>
/* Main title (st.title renders as h1) */
h1 {
    font-size: 4.5rem !important; /* Approximately 2x default st.title (2.25rem) */
}

/* Subheaders (st.subheader renders as h3) */
h3 {
    font-size: 3.25rem !important; /* Approximately 2x default st.subheader (1.625rem) */
}

/* Expander titles (text inside details > summary) */
details > summary {
    font-size: 3.75rem !important; /* Increased from 3.25rem to make it more visibly larger */
}

/* st.info and st.success messages (text inside .stAlert) */
.stAlert > div > div > p {
    font-size: 2rem !important; /* Approximately 2x default text size (around 1rem) */
}

/* Copyright text */
.footer-text {
    font-size: 1.5rem !important; /* Larger than default, adjust as needed */
}
</style>
""", unsafe_allow_html=True)


# 페이지 레이아웃을 넓게 설정합니다.
st.set_page_config(layout="wide")

# 앱의 제목을 설정합니다.
# st.title 대신 markdown으로 직접 h1 태그를 사용하여 스타일을 적용합니다.
st.markdown('<h1>중학교 과학에서 CT문제 해결!</h1>', unsafe_allow_html=True)

# 외부 HTML 파일들을 읽어옵니다.
# 실제 환경에서는 이 파일들이 존재해야 합니다.
try:
    with open('./index1.html', 'r', encoding='utf-8') as f:
        html1 = f.read()
except FileNotFoundError:
    html1 = "<h1>index1.html 파일을 찾을 수 없습니다.</h1><p>파일 경로를 확인해주세요.</p>"
    st.error("index1.html 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요.")

try:
    with open('./index2.html', 'r', encoding='utf-8') as f:
        html2 = f.read()
except FileNotFoundError:
    html2 = "<h1>index2.html 파일을 찾을 수 없습니다.</h1><p>파일 경로를 확인해주세요.</p>"
    st.error("index2.html 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요.")

try:
    with open('./index3.html', 'r', encoding='utf-8') as f:
        html3 = f.read()
except FileNotFoundError:
    html3 = "<h1>index3.html 파일을 찾을 수 없습니다.</h1><p>파일 경로를 확인해주세요.</p>"
    st.error("index3.html 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요.")

# 모든 콘텐츠를 담을 단일 메인 컬럼을 생성합니다.
# 각 과학 주제 내부에서 HTML 내용과 CT 요소를 위한 서브 컬럼을 나눕니다.
main_col, = st.columns(1)

with main_col:
    # '식물 잎의 개수 구하기' 주제 섹션
    with st.expander('식물 잎의 개수 구하기'):
        # 이 expander 내부에 HTML 내용과 CT 요소를 위한 두 개의 서브 컬럼을 생성합니다.
        sub_col_html, sub_col_ct = st.columns((3, 2)) # HTML 내용을 더 넓게, CT 요소를 좁게 설정

        with sub_col_html:
            st.subheader('문제 내용') # This will be styled by h3 CSS
            htmlviewer.html(html1, height=1200) # HTML 콘텐츠 표시

        with sub_col_ct:
            st.subheader('CT 요소') # This will be styled by h3 CSS
            # CT 요소: 문제분해
            with st.expander('문제분해'):
                st.info('문제를 작은 단위로 나누고 구조를 파악합니다. 예를 들어, 잎을 세는 과정을 작은 단계로 나눕니다: 잎 인식 → 잎 개수 세기 → 결과 기록.')

            # CT 요소: 추상화
            with st.expander('추상화'):
                st.success('중요한 정보만 남기고 불필요한 세부사항은 제거합니다. 예를 들어, 잎의 모양이나 크기보다는 단순히 "잎이 있다/없다"라는 핵심 정보에 집중합니다.')

            # CT 요소: 패턴인식
            with st.expander('패턴인식'):
                st.success('유사한 문제나 규칙, 반복되는 형태를 찾습니다. 예를 들어, 다른 식물에서도 잎을 세는 방식이 유사한지, 또는 특정 잎 모양이 반복되는지 확인합니다.')

    st.markdown('---') # 각 주제 섹션 간 구분선

    # '역학적 에너지 보존' 주제 섹션
    with st.expander('역학적 에너지 보존'):
        # 이 expander 내부에 HTML 내용과 CT 요소를 위한 두 개의 서브 컬럼을 생성합니다.
        sub_col_html, sub_col_ct = st.columns((3, 2))

        with sub_col_html:
            st.subheader('문제 내용')
            htmlviewer.html(html2, height=1200) # HTML 콘텐츠 표시

        with sub_col_ct:
            st.subheader('CT 요소')
            # CT 요소: 문제분해
            with st.expander('문제분해'):
                st.info('역학적 에너지 보존 문제를 운동 에너지와 위치 에너지의 변화로 분해하고, 각 에너지 형태가 시간에 따라 어떻게 변하는지 분석합니다.')

            # CT 요소: 추상화
            with st.expander('추상화'):
                st.success('공기 저항이나 마찰과 같은 불필요한 요소를 제거하고, 이상적인 상황에서 에너지 보존 법칙의 핵심 원리에 집중합니다.')

            # CT 요소: 패턴인식
            with st.expander('패턴인식'):
                st.success('다양한 상황(예: 진자 운동, 자유 낙하)에서 운동 에너지와 위치 에너지의 합이 일정하게 유지되는 패턴을 찾아냅니다.')

    st.markdown('---') # 각 주제 섹션 간 구분선

    # '빛의 3원색을 이용한 빛의 색 찾기' 주제 섹션
    with st.expander('빛의 3원색을 이용한 빛의 색 찾기'):
        # 이 expander 내부에 HTML 내용과 CT 요소를 위한 두 개의 서브 컬럼을 생성합니다.
        sub_col_html, sub_col_ct = st.columns((3, 2))

        with sub_col_html:
            st.subheader('문제 내용')
            htmlviewer.html(html3, height=1200) # HTML 콘텐츠 표시

        with sub_col_ct:
            st.subheader('CT 요소')
            # CT 요소: 문제분해
            with st.expander('문제분해'):
                st.info('빛의 색을 찾는 문제를 빨강, 초록, 파랑 세 가지 기본 색의 조합으로 분해하고, 각 색이 혼합될 때 어떤 결과가 나오는지 단계별로 파악합니다.')

            # CT 요소: 추상화
            with st.expander('추상화'):
                st.success('빛의 파장이나 강도와 같은 복잡한 물리적 특성보다는, 색의 혼합 결과에만 집중하여 핵심적인 색상 조합 규칙을 추출합니다.')

            # CT 요소: 패턴인식
            with st.expander('패턴인식'):
                st.success('빨강, 초록, 파랑의 다양한 조합이 어떤 새로운 색을 만들어내는지 반복되는 규칙(예: 빨강+초록=노랑)을 찾아냅니다.')

# 하단 구분선 및 저작권 표시
st.markdown('<hr>', unsafe_allow_html=True)
# Apply custom class for styling
st.markdown('<p class="footer-text"><font color="BLUE">(c)copyright. all rights reserved by Hwang</font></p>', unsafe_allow_html=True)
