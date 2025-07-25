import streamlit as st

st.title("🔐 AES 암호화/복호화 실전 웹앱")

st.header("1. 암호화란?")
st.markdown("""
- **암호화**는 평문(Plaintext, 원본 데이터)을 알고리즘과 '키'로 암호문(Ciphertext)으로 변환하는 과정입니다.
- 데이터를 안전하게 보호합니다.
""")

st.header("2. 복호화란?")
st.markdown("""
- **복호화**는 암호문을 다시 평문으로 돌려놓는 과정입니다.
- 암호화 때 사용한 '키'가 반드시 필요합니다.
""")

st.header("3. AES (Advanced Encryption Standard)")
st.markdown("""
- 미국 정부 표준, 가장 널리 쓰이는 대칭키 블록 암호화 알고리즘입니다.
- **대칭키**: 암호화/복호화에 같은 키를 사용합니다.
- **키 길이**: 16, 24, 32 바이트(128/192/256비트)만 허용합니다.
- 데이터를 16바이트씩 잘라 암호화합니다.
""")

st.header("4. CBC 모드란?")
st.markdown("""
- **CBC(Cipher Block Chaining)**: 각 블록 암호화 결과가 다음 블록에 반영되어 보안성이 높아집니다.
- 암호화할 때마다 무작위 IV(초기화 벡터)를 사용해 결과가 매번 다릅니다.
""")

st.header("5. 실전 사용 팁")
st.markdown("""
- **키 관리**가 매우 중요합니다. 키가 유출되면 보안이 무력화됩니다.
- AES는 금융, 정부, 산업 등에서 표준적으로 사용됩니다.
""")

st.info("좌측 상단 [≡] 메뉴에서 '암호화하기' 또는 '복호화하기' 페이지로 이동하세요!")